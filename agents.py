# In this Agent we are going to create 2 subagents. And these agents are basically used as tools to help the main agent to complete the task. 
# The main agent will be responsible for coordinating the subagents and providing the final output to the user.

from langchain.agents import create_agent
from langchain.tools import tool
from langchain.messages import HumanMessage
from models import openai_model
from tools import search_web
import logging

# CONFIGURE LOGGING
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# SUBAGENTS:- These subagents are responsible for searching the web for information related to wedding planning.
logging.info("initializing subagent1...")
subagent1 = create_agent(model = openai_model, tools = [search_web], name = "SubAgent1", description = "This agent is responsible for searching the web for information related to wedding planning.")

logging.info("initializing subagent2...")
subagent2 = create_agent(model = openai_model, tools = [search_web], name = "SubAgent2", description = "This agent is responsible for searching the web for information related to wedding planning.")

# Call the Tool (This tool is delegating[particular] tasks for our agents)
 
"""Whenever our main agent would like to give a task 
to another agent, it simply use this tool , 
give the query that what main agent would like to search.
This query will be passed to the subagent1 by invoking the agent1 
and the subagent1 will search the web for the query and return the results to the main agent."""


@tool
def delegate_to_subagent1(query: str)->str:
    # Search the web for a given topic by delegating the task to SubAgent1 and return the results
    logging.info("Delegating query to Subagent1: {query}")
    response = subagent1.invoke({"messages":[HumanMessage(content=query)]})
    return response["messages"][-1].content


@tool
def delegate_to_subagent2(query: str)->str:
    # Search the web for a given topic by delegating the task to SubAgent2 and return the results
    logging.info("Delegating query to Subagent2: {query}")
    response = subagent2.invoke({"messages":[HumanMessage(content=query)]})
    return response["messages"][-1].content

# Note:- In this project or any different project, We want to give an agent just one thing to do at a time. So we are creating 2 tools for 2 subagents.
# we have 2 subagents and each subagent is responsible for searching the web for information related to wedding planning.
