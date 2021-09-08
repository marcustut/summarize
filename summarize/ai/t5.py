import json
from typing import Optional
from summarize.scraper import parser
from summarize.utilities import capitalise_propn

from .helper import hf_inference_request, T5_MAX_CHUNK


def summarize(
    text: str,
    api_token: str,
    min_length: Optional[int] = 0,
    max_length: Optional[int] = 100,
) -> str:
    # input = parser.chunk_text(text, T5_MAX_CHUNK)

    response = hf_inference_request(
        text,
        "t5-base",
        api_token=api_token,
        min_length=min_length,
        max_length=max_length,
    )

    if not isinstance(response, list):
        return json.dumps(response)

    return capitalise_propn(response[0]["summary_text"])
