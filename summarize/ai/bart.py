from transformers import pipeline, Pipeline
from summarize.ai.summarizer import Summarizer
from summarize.scraper import parser


class Bart(Summarizer):
    def __init__(self):
        super().__init__(500)

    # Overrides abstract method
    def create_model(self) -> Pipeline:
        summarizer = pipeline("summarization")
        return summarizer

    # The content variable should be chunked
    def summarize(self, content: str, min_length: int, max_length: int) -> str:
        # Load BART model using pipeline
        text = parser.chunk_text(content, self.max_chunk)
        summarizer = self.create_model()
        return super().summarize(summarizer, text, min_length, max_length)
