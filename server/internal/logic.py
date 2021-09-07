from summarize.ai import naive, textrank, bart, t5, pegasus
from model.summarize import SummarizeMethods


class SummarizeMethodNotSupported(Exception):
    pass


def handleSummarize(
    method: SummarizeMethods, text: str, percentage: int, api_token: str
) -> str:

    max_length = len(text) * percentage

    if method == SummarizeMethods.Naive:
        return naive.summarize(text)

    elif method == SummarizeMethods.Textrank:
        return textrank.summarize(text, percentage)

    elif method == SummarizeMethods.Bart:
        return bart.summarize(text, api_token=api_token, max_length=max_length)

    elif method == SummarizeMethods.T5:
        return t5.summarize(text, api_token=api_token, max_length=max_length)

    elif method == SummarizeMethods.Pegasus:
        return pegasus.summarize(text, api_token=api_token, max_length=max_length)

    else:
        raise SummarizeMethodNotSupported(f"Method {method} is not supported")
