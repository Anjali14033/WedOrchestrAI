from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

openai_model = init_chat_model("gpt-5-nano", model_provider="openai")
print(openai_model.invoke("Hello, how are you?").content)

