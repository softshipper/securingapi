import os

from dotenv import load_dotenv
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from gotrue.types import User
from supabase import Client, create_client

load_dotenv()
router = APIRouter()

# 1) Initialize the Supabase client
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")  # or service_role key
supabase: Client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

# 2) Set up a FastAPI dependency to get and verify the Bearer token
security = HTTPBearer()


def get_current_user(
    token: HTTPAuthorizationCredentials = Depends(security),
) -> User:
    # The token will have the form "Bearer <access_token>"
    access_token = token.credentials

    # 3) Use Supabase’s auth.api to get the user
    resp = supabase.auth.get_user(access_token)
    resp.user

    # If invalid or not found, raise an exception
    if not resp.user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )

    # 4) Optionally do additional checks on the user or claims here
    return resp.user


@router.get("/")
def update_admin(current_user: User = Depends(get_current_user)):
    # current_user will contain the user data from Supabase (including email, role, etc.)
    return current_user
