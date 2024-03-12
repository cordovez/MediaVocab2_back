from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional


class Opinion(BaseModel):
    headline: Optional[str] = None
    teaser: Optional[str] = None
    author: Optional[str] = None
    published: Optional[str] = None
    content: Optional[str] = None


class OpinionRead(Opinion):
    id: ObjectId = Field(alias="_id")

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
