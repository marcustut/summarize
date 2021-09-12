# Author: Lee Kai Yang

import json
from summarize.scraper import parser
from typing import Optional

from .helper import PEGASUS_MAX_CHUNK, hf_inference_request


def summarize(
    text: str,
    api_token: str,
    min_length: Optional[int] = 0,
    max_length: Optional[int] = 100,
) -> str:
    # input = parser.chunk_text(text, PEGASUS_MAX_CHUNK)

    response = hf_inference_request(
        text,
        "google/pegasus-xsum",
        api_token=api_token,
        min_length=min_length,
        max_length=max_length,
    )

    if not isinstance(response, list):
        return json.dumps(response)

    return response[0]["summary_text"]
