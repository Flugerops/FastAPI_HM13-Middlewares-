from typing import Callable

from fastapi import Request, Response, HTTPException, status


async def header_check(request: Request, call_next: Callable) -> Response:
    if "/api" in request.url.path:
        if "X-Custom-Header" not in request.headers:
            return Response(
                "Missing Custom Header", status_code=status.HTTP_400_BAD_REQUEST
            )
    response = await call_next(request)
    return response
