from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import routers

app = FastAPI(
    docs_url="/",
)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(routers.router)