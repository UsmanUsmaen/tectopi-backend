from ai_core.llm import run_llm

class BaseAgent:
    def __init__(self, name, system_prompt):
        self.name = name
        self.system_prompt = system_prompt

    def run(self, user_input, context=None):
        context_text = f"\nContext:\n{context}" if context else ""

        prompt = f"""
SYSTEM:
{self.system_prompt}

USER:
{user_input}
{context_text}

Give practical advice suitable for Nigeria.
"""

        response = run_llm(prompt)

        return {
            "agent": self.name,
            "response": response
        }
