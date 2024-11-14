from fastapi import FastAPI

from .routes import api_router
from .middlewares import log_requests, header_check


app = FastAPI()

app.middleware("http")(log_requests)
app.middleware("http")(header_check)

app.include_router(api_router)
