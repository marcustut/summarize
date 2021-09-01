import sys
import re
import argparse

from summarize.ai import textrank
from summarize.ai import naive, Bart, Pegasus, T5
from summarize.scraper import parser
from typing import List


def _is_valid_url(url: str) -> bool:
    regex = re.compile(
        r"^(?:http|ftp)s?://"  # http:// or https://
        # domain...
        r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"
        r"localhost|"  # localhost...
        r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # ...or ip
        r"(?::\d+)?"  # optional port
        r"(?:/?|[/?]\S+)$",
        re.IGNORECASE,
    )

    return re.match(regex, url) is not None


def set_max_length(length: str) -> int:
    max_dict = {"short": 200, "medium": 600, "long": 1000}

    return max_dict.get("length")


def summarize_url(
    url: str, tags: List[str] = ["p"], method: str = "naive", length: str = "short"
):
    # Get the content from the url
    content = parser.parse_html_to_paragraphs(url, tags)

    # If no content is fetched
    if content == "":
        print(f"No content of {tags} is fetched from {url}")
        sys.exit(0)

    # Set summary length
    min_length = 1
    max_length = set_max_length(length)

    summary = ""

    # Summarize the content
    if method == "naive":
        summary = naive.summarize(content)
    elif method == "textrank":
        summary = textrank.summarize(content, 0.05)
    elif method == "bart":
        bart = Bart()
        summary = bart.summarize(content, min_length, max_length)
    elif method == "pegasus":
        pegasus = Pegasus()
        summary = pegasus.summarize(content, min_length, max_length)
    elif method == "t5":
        t5 = T5()
        summary = t5.summarize(content, min_length, max_length)

    # Print the summary to stdout
    print(summary)

    # Exits program successfully
    sys.exit(0)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="the website's url", type=str)
    parser.add_argument(
        "-t",
        "--tags",
        help="tags that is read from the website, eg. --tag p h1 h2",
        default=["p"],
        nargs="*",
    )
    parser.add_argument(
        "-m",
        "--method",
        help="method used for summarizing (naive, textrank, seq2seq)",
        default="naive",
        choices=["naive", "textrank", "seq2seq", "bart", "t5", "pegasus"],
    )
    # Add an argument for specifying 'short, medium, long'
    parser.add_argument(
        "-l",
        "--length",
        help="the length of the summary",
        type=str,
        default="short",
        choices=["short", "medium", "long"],
    )

    # Parse the arguments
    args = parser.parse_args()

    # Validate the url
    if not _is_valid_url(args.url):
        parser.error("url must be a valid url eg. https://www.google.com")

    # Summarize the website url
    summarize_url(args.url, args.tags, args.method, args.length)


if __name__ == "__main__":
    main()
