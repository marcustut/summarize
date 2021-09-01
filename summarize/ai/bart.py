from transformers import pipeline, Pipeline
from summarize.ai import Summarizer
from summarize.scraper import parser


class Bart(Summarizer):
    # Overrides abstract method
    def create_model() -> Pipeline:
        summarizer = pipeline("summarization")
        return summarizer

    # The content variable should be chunked
    def summarize(content: str, min_length: int, max_length: int) -> str:
        # Load BART model using pipeline
        text = parser.chunk_text(content)
        summarizer = super().create_model()
        super().summarize(summarizer, text, min_length, max_length)
