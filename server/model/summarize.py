from enum import Enum


class SummarizeTypes(str, Enum):
    Text = "text"
    Url = "url"


class SummarizeMethods(str, Enum):
    Naive = "naive"
    Textrank = "textrank"
    Bart = "bart"
    Pegasus = "pegasus"
    T5 = "t5"
