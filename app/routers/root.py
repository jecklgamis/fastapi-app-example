from fastapi import APIRouter

router = APIRouter(tags=["root"])


@router.get("/")
async def root() -> dict[str, str]:
    return {"message": "It works on my machine!", "app": "fastapi-app-template"}
