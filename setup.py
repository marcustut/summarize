from setuptools import setup, find_packages

setup(
    name="summarize",
    version="0.1",
    description="Summarize texts from a website given its URL",
    author="Marcus Lee & Liana Ling",
    author_email="marcustutorial@hotmail.com & lianalingliya@gmail.com",
    packages=find_packages(),
    install_requires=["requests", "bs4", "nltk", "transformers", "pandas"],
)
