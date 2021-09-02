import requests
from bs4 import BeautifulSoup
from typing import List


def _get_html_text(url: str) -> str:
    # Fetch the HTML content and return it as text
    return requests.get(url).text


def parse_html_to_paragraphs(url: str, tags: List[str]) -> str:
    html_content = _get_html_text(url)

    # Parsing the URL content and storing in a variable
    parsed = BeautifulSoup(html_content, "html.parser")

    # Get all the content in the tas
    paragraphs = parsed.find_all(tags)

    content = ""

    # Looping through the paragraphs and adding them to the variable
    for paragraph in paragraphs:
        content += paragraph.text

    return content


# The content variable should be parsed into paragraphs
# Used by BART
def chunk_text(content: str, max_chunk: int) -> List[str]:
    current_chunk = 0
    chunks = []

    for sentence in content:
        if len(chunks) == current_chunk + 1:
            # Check if the chunk is less than 500 words
            if len(chunks[current_chunk]) + len(sentence.split(" ")) <= max_chunk:
                chunks[current_chunk].extend(sentence.split(" "))
            # Next chunk
            else:
                current_chunk += 1
                chunks.append(sentence.split(" "))
        else:
            print(current_chunk)
            chunks.append(sentence.split(" "))

    # Append words to chunks so that each chunk is less than 500 words
    for chunk_id in range(len(chunks)):
        chunks[chunk_id] = " ".join(chunks[chunk_id])

    return chunks
