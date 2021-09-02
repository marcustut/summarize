from typing import List
import stanfordnlp as stfnlp

# Used by models using HuggingFace pipeline functions to
# To convert a returned summary of type List["dict[str str]"] to a concatenated string
def append(raw_summary: list("dict[str, str]")) -> str:
    for d in raw_summary:
        summary = "".join(str(val.capitalize()) + "\n" for _, val in d.items())

        # Remove extra spaces
        summary = summary.replace(" .", ".")
        summary = summary.replace(" !", "!")
        summary = summary.replace(" ?", "?")
        return summary


# Uses stanfordnlp to do POS tagging and capitalises proper nouns
# Used by models whose output is without proper formatting, such as T5
def capitalise_propn(summary: str) -> str:
    # Capitalise proper nouns and do post-processing
    doc_list = _add_spaces_and_sentence_case(summary)
    return _list_to_string(doc_list)


# INTERNAL FUNCTIONS FOR capitalise_propn ONLY, START --------------------------
def _load_stf_model():
    stfnlp.download("en")


def _create_pipeline_pos() -> stfnlp.Pipeline:
    return stfnlp.Pipeline(processors="tokenize,mwt,pos")


def _tag_pos(stf_nlp: stfnlp.Pipeline, summary: str) -> stfnlp.Document:
    return stf_nlp(summary)


# Preprocesses input summary with POS tagging
def _analyse_summary(summary: str) -> stfnlp.Document:
    _load_stf_model()
    stf_nlp = _create_pipeline_pos()
    return _tag_pos(stf_nlp, summary)


def _capitalise_propn(summary: str, doc: stfnlp.Document) -> List[str]:
    return [
        w.text.capitalize() if w.upos in ["PROPN", "NNS"] else w.text
        for sent in doc.sentences
        for w in sent.words
    ]


def _add_spaces_and_sentence_case(summary: str) -> List[str]:
    doc = _analyse_summary(summary)
    doc_list = _capitalise_propn(summary, doc)
    i = 0
    for sent in doc.sentences:
        for w in range(len(sent.words)):
            if w != 2:
                if sent.words[w - 1].xpos in ["!", "."]:  # Capitalise each first word
                    doc_list[i] = sent.words[w].text.capitalize()
            if (
                sent.words[w].upos != "PUNCT" and i != 0
            ):  # Add a space before non-punctuation words
                doc_list[i] = " " + doc_list[i]
            i += 1
    return doc_list


def _list_to_string(doc_list: List[str]) -> str:
    summary = ""
    for s in doc_list:
        summary += s
    return summary


# INTERNAL FUNCTIONS END -------------------------------------------------------
