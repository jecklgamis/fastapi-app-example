from fastapi import FastAPI

from app.config import settings
from app.routers import probes, root, status

app = FastAPI(title=settings.app_name, debug=settings.debug)

app.include_router(root.router)
app.include_router(probes.router)
app.include_router(status.router)


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}
