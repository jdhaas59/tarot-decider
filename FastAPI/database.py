import os
from dotenv import load_dotenv

from supabase import Client, create_client


# Load variables from .env file in the root directory
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

# Access the variables
api_url: str = os.getenv("DB_URL")
api_key: str = os.getenv("API_KEY")


def create_supabase_client():
    supabase: Client = create_client(api_url, api_key)
    return supabase