import os
import requests

from supabase import create_client, Client
from dotenv import load_dotenv


load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

# Sign in the user
user_credentials = {"email": "info@agentswarm.tech", "password": "RZ;X4cR$sQ~d_+dH"}
response = supabase.auth.sign_in_with_password(user_credentials)

print("Your token:", response.session.access_token)

headers = {
    "Authorization": f"Bearer {response.session.access_token}"
}
admin_url = "http://127.0.0.1:8000/admin/"
admin_response = requests.get(admin_url, headers=headers)
print(admin_response.json())