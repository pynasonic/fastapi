from pydantic import BaseModel
from typing   import List

class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        schema_extra = {
            "example":{
                "title": "FastAPI Book",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will do it.",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "zoom place"
            }
        }