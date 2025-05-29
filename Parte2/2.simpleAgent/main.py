from dotenv import load_dotenv
from langchain.tools import Tool
from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import init_chat_model

def calc(operation: str) ->str:
    try:
        return str(eval(operation))
    except Exception as err:
        return f"[ERROR] {err}"
    
calculator_tool = Tool(
    name="Calculator",
    description="Do a basic math operation",
    func=calc
)

# loads key from environment
load_dotenv()

# load llm
llm = init_chat_model(
    "anthropic:claude-3-5-sonnet-latest",
    temperature=0, # Consistent answers (good for math operations)
    max_tokens=1024 # max_tokens required
)

"""
ZERO_SHOT_REACT_DESCRIPTION
ZERO_SHOT --> No examples before
REACT --> REasoning+ACTing (thought pattern)
DESCRIPTION --> Use tool description to choose a tool

"""

agent = initialize_agent(
    tools=[calculator_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose = True,
    handle_parsing_errors = True
)

if __name__ == "__main__":
    # RUNNING THIS CODE WILL THROW AN ERROR [API KEY WAS REMOVED FOR SAFETY REASONS]
    response = agent.run(
        "(3 * 7) + 5"
    )
    print(response)
