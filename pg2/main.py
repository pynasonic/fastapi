from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from data.movie_db import fake_movie_db

class Movie(BaseModel):
    name: str
    plot: str
    genres: List[str]
    casts: List[str]



app = FastAPI()


@app.get('/', response_model=List[Movie])
async def index():
    return fake_movie_db