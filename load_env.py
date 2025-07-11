from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

# Get OpenAI API key from environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")
print("Loaded API Key:", openai_api_key[:8] + "..." if openai_api_key else "Not Found")
