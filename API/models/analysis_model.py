from pydantic import BaseModel, Field
from typing import Optional


class TextAnalysis(BaseModel):
    article_id: str
    article_url: str
    verbs: Optional[list] = None
    adjectives: Optional[list] = None
    adverbs: Optional[list] = None
    entities: Optional[list] = None
    phrasal_verbs: Optional[dict] = None


class AnalysisRead(TextAnalysis):
    id: str = Field(alias="_id")
