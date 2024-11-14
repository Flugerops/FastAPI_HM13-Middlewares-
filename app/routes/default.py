from typing import Annotated

from fastapi import APIRouter, Header

from ..middlewares import header_check


api_router = APIRouter(prefix="/api")


@api_router.get("/")
async def home(X_Custom_Header: Annotated[str | None, Header()] = None):
    return {"header": X_Custom_Header}
