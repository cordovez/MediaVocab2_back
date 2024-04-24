from spacy.tokens import Doc


def extract_phrasal_verbs(spacy_document: Doc) -> dict:
    phrasal_verbs = {}
    for token in spacy_document:
        if token.pos_ == "VERB":
            for child in token.children:
                if child.pos_ == "ADP" and child.dep_ == "prt":
                    phrasal_verb = f"{token.text} {child.text}"
                    phrase_positions = (token.idx, child.idx + len(child.text))
                    if phrasal_verb not in phrasal_verbs:
                        phrasal_verbs[phrasal_verb] = [phrase_positions]
                    else:
                        phrasal_verbs[phrasal_verb].append(phrase_positions)
                    break
    return phrasal_verbs


def extract_entities(spacy_document):  # sourcery skip: use-any, use-next
    entities = []
    for ent in spacy_document.ents:
        if ent.label_ not in ["ORDINAL", "CARDINAL", "DATE"]:
            found = False
            for ent_dict in entities:
                if ent.text in ent_dict:
                    found = True
                    break
            if not found:
                entities.append({ent.text: ent.label_})

    return entities
