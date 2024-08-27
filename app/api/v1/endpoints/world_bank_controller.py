from fastapi import APIRouter
from app.scraping import world_wide


router = APIRouter(prefix="/api/v1/worldbank")

@router.get("/search")
async def get_result(input: str):
    return world_wide.search(input)