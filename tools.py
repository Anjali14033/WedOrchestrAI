from langchain.tools import tool
from tavily import TavilyClient
from dotenv import load_dotenv
import logging

# CONFIGURE LOGGING
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# LOAD ENVIRONMENT VARIABLES
load_dotenv()

# INITIALIZE TAVILY CLIENT
tavily_client = TavilyClient()

#TOOL CREATION
@tool
def search_web(topic: str) -> str:
    """Search the web for a given topic and return the results"""
    # Whenever our agent is using our tool, we will be logging it to understand that what is our agent Searching
    logging.info(f"Searching the web for topic: {topic}")
    results = tavily_client.search(topic)
    return results
    

