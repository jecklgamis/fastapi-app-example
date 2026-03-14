import json
from pathlib import Path
from typing import Any

from fastapi import APIRouter

router = APIRouter()

_BUILD_INFO_PATH = Path("build-info.json")

_DEFAULT_BUILD_INFO: dict[str, str] = {
    "app": "fastapi-app-template",
    "version": "0.1.0",
    "git_commit": "unknown",
    "git_branch": "unknown",
    "build_timestamp": "unknown",
}


def _load_build_info() -> dict[str, Any]:
    if _BUILD_INFO_PATH.exists():
        return json.loads(_BUILD_INFO_PATH.read_text())  # type: ignore[no-any-return]
    return _DEFAULT_BUILD_INFO


@router.get("/build-info")
async def build_info() -> dict[str, Any]:
    return _load_build_info()
