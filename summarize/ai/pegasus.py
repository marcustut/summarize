from transformers import (
    PegasusForConditionalGeneration,
    PegasusTokenizer,
    pipeline,
    Pipeline,
)
from summarize.utilities import append
from summarize.ai.summarizer import Summarizer
from summarize.scraper import parser

from summarize.utilities import append


class Pegasus(Summarizer):
    def __init__(self):
        super().__init__(self, max_chunk=250)

    # Overrides abstract method
    def create_model() -> Pipeline:
        model_name = "google/pegasus-xsum"
        # torch_device = "cuda"
        tokenizer = PegasusTokenizer.from_pretrained(model_name)
        model = PegasusForConditionalGeneration.from_pretrained(model_name)
        summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)
        return summarizer

    # The content variable should be parsed into paragraphs
    def summarize(self, content: str, min_length: int, max_length: int) -> str:
        # Load pegasus model using pipeline
        text = parser.chunk_text(content, self.max_chunk)
        summarizer = self.create_model()
        return super().summarize(summarizer, text, min_length, max_length)
