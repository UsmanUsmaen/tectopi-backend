from agents.support import support_agent
from agents.finance import finance_agent
from agents.education import education_agent

AGENTS = {
    "support": support_agent,
    "finance": finance_agent,
    "education": education_agent
}

def get_agent(name: str):
    return AGENTS.get(name)
