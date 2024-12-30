from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def danger_zone():
    return {"message": "Admin getting schwifty"}
