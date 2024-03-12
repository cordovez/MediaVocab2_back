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
    id: str = Field(alias="_id")

    #     id: Optional[ObjectId] = Field(alias="_id")

    class Config:
        #         arbitrary_types_allowed = True
        #         json_encoders = {ObjectId: str}
        json_schema_extra = {
            "example": {
                "id": "65f010b6b15eb75edca25a51",
                "headline": "Opinion Headline",
                "teaser": "Opinion Teaser",
                "author": "Juan Carlos Cordovez-Mantilla",
                "published": "Sun 10 Mar 2024 09.00 CET",
                "content": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Possimus, at eaque. Sapiente voluptatem totam recusandae provident corrupti neque veniam assumenda, non id reiciendis exercitationem illo tempora aperiam veritatis aliquid quibusdam ullam fuga omnis temporibus ratione quam nobis nostrum perspiciatis cum! Aspernatur tempore odit qui non perferendis inventore rem? Recusandae, voluptas?",
            }
        }
