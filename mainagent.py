from prompt import WEDDING_PLANNER_AGENT_PROMPT, USER_PROMPT_FOR_MAIN_AGENT
from langchain.agents import create_agent
from models import openai_model
from agents import delegate_to_subagent1, delegate_to_subagent2
import logging
from langchain.messages import HumanMessage

#Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Asking user for their requirements for their wedding
logging.info("Asking user for their wedding requirements...")
user_requirements = input("Please enter your requirements and preferences for your wedding\n")


#Updating the System prompt with the user requirements
updated_system_prompt = WEDDING_PLANNER_AGENT_PROMPT.format(requirements=user_requirements)


# MAIN AGENT CREATION
logging.info("Initializing main wedding planner agent...")
main_wedding_agent = create_agent(
    model=openai_model,
    tools=[delegate_to_subagent1, delegate_to_subagent2],
    name="WeddingPlannerAgent",
    system_prompt = updated_system_prompt,
    description="This agent is responsible for assisting the user in planning their wedding by providing recommendations and suggestions based on their preferences and requirements."
)

# Invoke main agent with the user prompt
logging.info("Invoking main wedding planner agent with user prompt...")
response_main_wedding_agent = main_wedding_agent.invoke({"messages": [HumanMessage(content=USER_PROMPT_FOR_MAIN_AGENT)]})


#Printing the response of the main agent
print("\nMain Wedding Planner Agent Response: ")
print(response_main_wedding_agent['messages'][-1].content)