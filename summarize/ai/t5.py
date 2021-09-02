from transformers import pipeline, Pipeline
from summarize.ai.summarizer import Summarizer
from summarize.scraper import parser


class T5(Summarizer):
    # Overrides abstract method
    def create_model() -> Pipeline:
        summarizer = pipeline(
            "summarization", model="t5-base", tokenizer="t5-base", framework="pt"
        )
        return summarizer

    # The content variable should be chunked
    def summarize(self, content: str, min_length: int, max_length: int) -> str:
        # Load T5 model using pipeline
        text = parser.chunk_text(content)
        summarizer = self.create_model()
        super().summarize(summarizer, text, min_length, max_length)
