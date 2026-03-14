from fastapi import APIRouter

router = APIRouter(prefix="/probe", tags=["probe"])


@router.get("/live")
async def live() -> dict[str, str]:
    return {"status": "I'm alive!"}


@router.get("/ready")
async def ready() -> dict[str, str]:
    return {"status": "I'm ready!"}


@router.get("/startup")
async def startup() -> dict[str, str]:
    return {"status": "started"}
