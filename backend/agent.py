from .memory import MemoryManager
from .supervisor import Supervisor
from .rag import RAGEngine
from .tools import ToolManager
from .llm import LLM
from .prompts import PERSONAS
from .logger import logger
import time
start = time.time()
class NPCAgent:

    def __init__(self):
        self.llm = LLM()
        self.memory = MemoryManager()
        self.supervisor = Supervisor()
        self.rag = RAGEngine()
        self.tools = ToolManager()

    def build_prompt(
        self,
        persona,
        history,
        context,
        tool_result,
        user_message
    ):

        persona_prompt = PERSONAS[persona]

        conversation = ""

        for turn in history[-8:]:

            conversation += f"""
User:
{turn["user"]}

Assistant:
{turn["assistant"]}

"""

        prompt = f"""

{persona_prompt}

=========================

Relevant Knowledge

{context}

=========================

Conversation

{conversation}

=========================

Tool Result

{tool_result}

=========================

Current User

{user_message}

Respond naturally.

"""

        return prompt


    def chat(
        self,
        session_id,
        persona,
        user_message
    ):

        history = self.memory.load(session_id)

        supervisor_state = self.supervisor.monitor(
            history,
            user_message
        )

        tool_result = ""

        if supervisor_state["tool"] is not None:

            tool_result = self.tools.run(
                supervisor_state["tool"],
                user_message
            )

        rag=self.rag.search(user_message)

        context=rag["context"]

        sources=rag["sources"]
        prompt = self.build_prompt(
            persona,
            history,
            context,
            tool_result,
            user_message
        )

        response = self.llm.invoke(

                prompt

        ).strip()
        latency = round(time.time() - start, 2)
        logger.info(
    f"Assistant: {response[:100]}"
)
        history.append({

            "user": user_message,

            "assistant": response

        })

        self.memory.save(
            session_id,
            history
        )

        return {

            "assistant_message": response,
            "sources":sources,
            "latency": latency,

            "state_update": {

                "turns": len(history),

                "relationship_score":
                    self.memory.relationship(session_id)

            },

            "safety_flags":
                supervisor_state["flags"]

        }
