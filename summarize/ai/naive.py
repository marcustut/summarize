# Author: Lee Kai Yang

import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from typing import List
from summarize.utilities import capitalise_propn


def summarize(text: str) -> str:

    # Tokenize the text by sentences
    sentences = nltk.sent_tokenize(text)

    # Calculate the scores of each sentence
    sentence_scores = _calculate_sentence_scores(
        sentences, _create_dictionary_table(text)
    )

    # Get the average score
    average_scores = _calculate_average_score(sentence_scores)

    # Compare each sentence to the average score
    # and get the highest score sentences
    summary = _get_article_summary(sentences, sentence_scores, average_scores)

    return summary


def _create_dictionary_table(text: str) -> dict:

    # Removing stop words
    stop_words = set(stopwords.words("english"))

    words = nltk.word_tokenize(text)

    # Reducing words to their root form
    stem = PorterStemmer()

    # Creating dictionary for the word frequency table
    frequency_table = dict()
    for wd in words:
        wd = stem.stem(wd)
        if wd in stop_words:
            continue
        if wd in frequency_table:
            frequency_table[wd] += 1
        else:
            frequency_table[wd] = 1

    return frequency_table


def _calculate_sentence_scores(sentences: List[str], frequency_table: dict) -> dict:

    # Algorithm for scoring a sentence by its words
    sentence_weight = dict()

    for sentence in sentences:
        # sentence_wordcount = (len(nltk.word_tokenize(sentence)))
        sentence_wordcount_without_stop_words = 0
        for word_weight in frequency_table:
            if word_weight in sentence.lower():
                sentence_wordcount_without_stop_words += 1
                if sentence[:7] in sentence_weight:
                    sentence_weight[sentence[:7]] += frequency_table[word_weight]
                else:
                    sentence_weight[sentence[:7]] = frequency_table[word_weight]

        sentence_weight[sentence[:7]] = (
            sentence_weight[sentence[:7]] / sentence_wordcount_without_stop_words
        )

    return sentence_weight


def _calculate_average_score(sentence_weight: dict) -> int:

    # Calculating the average score for the sentences
    sum_values = 0
    for entry in sentence_weight:
        sum_values += sentence_weight[entry]

    # Getting sentence average value from source text
    average_score = sum_values / len(sentence_weight)

    return average_score


def _get_article_summary(
    sentences: List[str], sentence_weight: dict, threshold: int
) -> str:

    sentence_counter = 0
    article_summary = ""

    for sentence in sentences:
        if sentence[:7] in sentence_weight and sentence_weight[sentence[:7]] >= (
            threshold
        ):
            article_summary += " " + sentence
            sentence_counter += 1

    return capitalise_propn(article_summary)
