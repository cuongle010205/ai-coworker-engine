import os
import json

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from pathlib import Path



class RAGEngine:

    def __init__(
        self,
        db_path=None,
        data_path=None
    ):

        base_dir = Path(__file__).resolve().parent.parent

        self.db_path = str(
            db_path if db_path is not None
            else base_dir / "vector_db"
        )

        self.data_path = str(
            data_path if data_path is not None
            else base_dir / "data" / "gucci_docs.json"
        )

        self.embeddings = HuggingFaceEmbeddings(
            model_name="BAAI/bge-small-en-v1.5"
        )

        print("Vector DB :", self.db_path)
        print("Data Path :", self.data_path)

        if os.path.exists(self.db_path):

            self.vector_db = FAISS.load_local(
                self.db_path,
                self.embeddings,
                allow_dangerous_deserialization=True
            )

        else:

            docs = self.load_documents()

            self.vector_db = FAISS.from_documents(
                docs,
                self.embeddings
            )

            self.vector_db.save_local(self.db_path)


    def load_documents(self):

        with open(
            self.data_path,
            "r",
            encoding="utf8"
        ) as f:

            data = json.load(f)

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=600,
            chunk_overlap=100
        )

        docs = []

        for item in data:

            docs.append(

                Document(

                    page_content=item["content"],

                    metadata={

                        "title": item.get("title", "")

                    }

                )

            )

        return splitter.split_documents(docs)

    def search(
    self,
    query,
    k=4
):

        docs = self.vector_db.similarity_search(
        query,
        k=k
    )

        context = ""

        sources = []

        for doc in docs:

            context += doc.page_content + "\n\n"

            sources.append(
            doc.metadata.get("title","Unknown")
        )

        return {

        "context":context,

        "sources":sources

    }


    def search_with_score(
        self,
        query,
        k=4
    ):

        return self.vector_db.similarity_search_with_score(
            query,
            k=k
        )