from fastapi import FastAPI
from api.movie_api import movies

app = FastAPI()

app.include_router(movies)