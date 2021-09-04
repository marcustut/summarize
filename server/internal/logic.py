from summarize.ai import naive, textrank
from model.summarize import SummarizeMethods


class SummarizeMethodNotSupported(Exception):
    pass


def handleSummarize(method: SummarizeMethods, text: str) -> str:
    if method == SummarizeMethods.Naive:
        return naive.summarize(text)
    elif method == SummarizeMethods.Textrank:
        return textrank.summarize(text, percentage=0.05)
    else:
        raise SummarizeMethodNotSupported(f"Method {method} is not supported")
