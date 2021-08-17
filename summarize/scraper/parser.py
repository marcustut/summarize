import requests
from bs4 import BeautifulSoup
from typing import List


def _get_html_text(url: str) -> str:
    # Fetch the HTML content and return it as text
    return requests.get(url).text


def parse_html_to_paragraphs(url: str, tags: List[str]) -> str:
    html_content = _get_html_text(url)

    # Parsing the URL content and storing in a variable
    parsed = BeautifulSoup(html_content, 'html.parser')

    # Get all the content in the tas
    paragraphs = parsed.find_all(tags)

    content = ''

    # Looping through the paragraphs and adding them to the variable
    for paragraph in paragraphs:
        content += paragraph.text

    return content
