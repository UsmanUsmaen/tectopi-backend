from fastapi import APIRouter
from api.ai import ai_router

router = APIRouter()
router.include_router(ai_router, prefix="/ai", tags=["AI"])
