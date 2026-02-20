from fastapi import APIRouter
from pydantic import BaseModel
from agents.registry import get_agent

ai_router = APIRouter()

class AIRequest(BaseModel):
    message: str
    context: dict | None = None

@ai_router.post("/{agent_name}")
def run_agent(agent_name: str, req: AIRequest):
    agent = get_agent(agent_name)
    if not agent:
        return {"error": "Agent not found"}
    return agent.run(req.message, req.context)
