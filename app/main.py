from fastapi import Depends, FastAPI

from dotenv import load_dotenv
from .internal import admin
from .routers import users

app = FastAPI()


app.include_router(users.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
