from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException
from .agent import NPCAgent
from fastapi.middleware.cors import CORSMiddleware
from .logger import logger
app = FastAPI()
app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_methods=["*"],

    allow_headers=["*"]
)
npc = NPCAgent()

class ChatRequest(BaseModel):

    session_id:str

    persona:str

    message:str

@app.post("/chat")
def chat(req: ChatRequest):
    logger.info(
        f"[{req.session_id}] {req.persona}: {req.message}"
    )

    try:

        return npc.chat(
            req.session_id,
            req.persona,
            req.message
        )

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    except Exception as e:

        logger.exception(e)

        raise HTTPException(
            status_code=500,
            detail="Internal server error."
        )
@app.get("/health")

def health():

    return {

        "status":"ok"

    }