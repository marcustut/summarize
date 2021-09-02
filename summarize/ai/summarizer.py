from abc import ABC, abstractmethod
from summarize.utilities import append
from transformers import Pipeline


class Summarizer(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def create_model():
        pass

    def summarize(
        summarizer: Pipeline, text: str, min_length: int, max_length: int
    ) -> str:
        summary = summarizer(text, min_length=min_length, max_length=max_length)
        return append(summary)
