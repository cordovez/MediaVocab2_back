from spacy.tokens import Doc


def extract_adjectives(spacy_document: Doc) -> list:
    adjectives = []
    for token in spacy_document:
        if token.pos_ == "ADJ":
            found = False
            for adj_dict in adjectives:
                if token.text in adj_dict:
                    adj_dict[token.text]["position"].append(token.i)
                    found = True
                    break

            if not found:
                adjectives.append({token.text: {"position": [token.i]}})

    return adjectives


def extract_adverbs(spacy_document: Doc) -> list:
    adverbs = []

    for token in spacy_document:
        if token.pos_ == "ADV":
            found = False
            for adv_dict in adverbs:
                if token.text in adv_dict:
                    adv_dict[token.text]["position"].append(token.i)

                    found = True
                    break

            if not found:
                adverbs.append({token.text: {"position": [token.i]}})
    return adverbs


def extract_nouns(spacy_object: Doc) -> list:
    nouns = []

    for token in spacy_object:
        if token.pos_ == "NOUN":
            found = False

            for noun_dict in nouns:
                if token.text in noun_dict:
                    noun_dict[token.text]["position"].append(token.i)

                    found = True
                    break

            if not found:
                nouns.append({token.text: {"position": [token.i]}})

    return nouns


def extract_verbs(spacy_document: Doc) -> list:
    verbs = []

    for token in spacy_document:

        if token.pos_ == "VERB":
            found = False
            for verb_dict in verbs:
                if token.lemma_ in verb_dict:
                    verb_dict[token.lemma_][str(token.i)] = token.text
                    found = True
                    break

            if not found:
                verbs.append({token.lemma_: {str(token.i): token.text}})

    return verbs
