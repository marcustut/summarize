from distutils import util
from transformers import pipeline, Pipeline
from summarize.ai.summarizer import Summarizer
from summarize.scraper import parser
from summarize.utilities import util


class T5(Summarizer):
    def __init__(self):
        super().__init__(self, max_chunk=500)

    # Overrides abstract method
    def create_model() -> Pipeline:
        summarizer = pipeline(
            "summarization", model="t5-base", tokenizer="t5-base", framework="pt"
        )
        return summarizer

    # The content variable should be chunked
    def summarize(self, content: str, min_length: int, max_length: int) -> str:
        # Load T5 model using pipeline
        text = parser.chunk_text(content, self.max_chunk)
        summarizer = self.create_model()
        summary = super().summarize(summarizer, text, min_length, max_length)
        return util.capitalise_propn(summary)
