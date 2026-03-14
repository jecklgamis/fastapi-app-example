import os
import platform
import sys
import time

import psutil
from fastapi import APIRouter, Depends

from app.basic_auth import verify_credentials

router = APIRouter(prefix="/status", tags=["status"])

_start_time = time.time()


@router.get("/")
async def system_status(
    username: str = Depends(verify_credentials),
) -> dict[str, object]:
    mem = psutil.virtual_memory()
    return {
        "app": {
            "version": "0.1.0",
            "uptime_seconds": round(time.time() - _start_time, 2),
        },
        "system": {
            "hostname": os.uname().nodename,
            "os": f"{platform.system()} {platform.release()}",
            "architecture": platform.machine(),
            "python_version": sys.version,
        },
        "resources": {
            "cpu_count": os.cpu_count(),
            "cpu_percent": psutil.cpu_percent(interval=0.1),
            "memory_total_mb": round(mem.total / 1024 / 1024),
            "memory_used_mb": round(mem.used / 1024 / 1024),
            "memory_percent": mem.percent,
        },
    }
