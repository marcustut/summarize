from typing import Optional
from summarize.ai import naive, textrank
from model.summarize import SummarizeMethods


class SummarizeMethodNotSupported(Exception):
    pass


def handleSummarize(method: SummarizeMethods, text: str, percentage: int) -> str:

    if method == SummarizeMethods.Naive:
        return naive.summarize(text)

    elif method == SummarizeMethods.Textrank:
        return textrank.summarize(text, percentage)

    else:
        raise SummarizeMethodNotSupported(f"Method {method} is not supported")
