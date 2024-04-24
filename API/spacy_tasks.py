from spacy.tokens import Doc

from helpers.pos_extraction import (
    extract_nouns,
    extract_adjectives,
    extract_adverbs,
    extract_verbs,
)
from helpers.phrase_extraction import extract_entities, extract_phrasal_verbs

from helpers.spacy_doc import create_spacy_doc


async def create_text_analysis(id: str) -> dict:
    doc: Doc = await create_spacy_doc(id)
    article_id: str = doc._.id
    article_url: str = doc._.url
    nouns: list = extract_nouns(doc)
    verbs: list = extract_verbs(doc)
    adjectives: list = extract_adjectives(doc)
    adverbs: list = extract_adverbs(doc)
    entities: list = extract_entities(doc)
    phrasal_verbs: dict = extract_phrasal_verbs(doc)

    return {
        "article_id": article_id,
        "article_url": article_url,
        "nouns": nouns,
        "verbs": verbs,
        "adjectives": adjectives,
        "adverbs": adverbs,
        "entities": entities,
        "phrasal_verbs": phrasal_verbs,
    }
