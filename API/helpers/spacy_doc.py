import spacy
from spacy.tokens import Doc

from db.db import get_one

nlp = spacy.load("en_core_web_sm")


async def fetch_text(id: str) -> dict:
    return await get_one(id)


async def create_spacy_doc(id: str) -> Doc:
    """
    Creates a spaCy Doc object from the text content fetched using the provided id.

    Args:
        id: The unique identifier used to fetch the text content.

    Returns:
        Doc: A spaCy Doc object created from the fetched text content.
    """

    Doc.set_extension("id", default=None, force=True)
    Doc.set_extension("url", default=None, force=True)
    article_dict = await fetch_text(id)
    doc = nlp(article_dict["content"])
    doc._.url: str = article_dict["url"]
    doc._.id: str = id

    return doc
