import os
from dotenv import load_dotenv

load_dotenv()

class Settings():

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")    # fetching api key from .env file

    MODEL_NAME = "llama-3.1-8b-instant"         # model name
    
    TEMPERATURE = 0.9                           # temperature jitna 1 ke karib hoga utna zyada creative responses milenge 

    MAX_RETRIES = 3                             # maximum retries for API calls


settings = Settings()  