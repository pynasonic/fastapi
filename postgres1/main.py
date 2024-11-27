from db_base import Base, engine
from models import Post  # Import all models
from routes import apirouter

from fastapi import FastAPI
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/create_tables")
async def ct():

    # Create all tables in the database
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")


app.include_router(apirouter)