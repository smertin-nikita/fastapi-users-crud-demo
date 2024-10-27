from fastapi import APIRouter
from starlette import status

router = APIRouter()

@router.get("/health", status_code=status.HTTP_200_OK)
async def create():
    return {"status": "ok"}