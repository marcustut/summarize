# Author: Lee Kai Yang

from heapq import nlargest

import pandas as pd
import re
from nltk import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from string import punctuation
from summarize.ai.helper import contractions_dict
from summarize.utilities import capitalise_propn

stop_words = set(stopwords.words("english"))
punctuation = punctuation + "\n" + "—" + "“" + "," + "”" + "‘" + "-" + "’"

contractions_re = re.compile("(%s)" % "|".join(contractions_dict.keys()))


# Function to clean the html from the article
def cleanhtml(raw_html):
    cleanr = re.compile("<.*?>")
    cleantext = re.sub(cleanr, "", raw_html)
    return cleantext


# Function expand the contractions if there's any
def expand_contractions(s, contractions_dict=contractions_dict):
    def replace(match):
        return contractions_dict[match.group(0)]

    return contractions_re.sub(replace, s)


# Function to preprocess the articles
def preprocessing(article):
    global article_sent

    # Converting to lowercase
    article = article.str.lower()

    # Removing the HTML
    article = article.apply(lambda x: cleanhtml(x))

    # Removing the email ids
    article = article.apply(lambda x: re.sub("\S+@\S+", "", x))

    # Removing The URLS
    article = article.apply(
        lambda x: re.sub(
            "((http\://|https\://|ftp\://)|(www.))+(([a-zA-Z0-9\.-]+\.[a-zA-Z]{2,4})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(/[a-zA-Z0-9%:/-_\?\.'~]*)?",
            "",
            x,
        )
    )

    # Removing the '\xa0'
    article = article.apply(lambda x: x.replace("\xa0", " "))

    # Removing the contractions
    article = article.apply(lambda x: expand_contractions(x))

    # Stripping the possessives
    article = article.apply(lambda x: x.replace("'s", ""))
    article = article.apply(lambda x: x.replace("’s", ""))
    article = article.apply(lambda x: x.replace("'s", ""))
    article = article.apply(lambda x: x.replace("\’s", ""))

    # Removing the Trailing and leading whitespace and double spaces
    article = article.apply(lambda x: re.sub(" +", " ", x))

    # Copying the article for the sentence tokenization
    article_sent = article.copy()

    # Removing punctuations from the article
    article = article.apply(
        lambda x: "".join(word for word in x if word not in punctuation)
    )

    # Removing the Trailing and leading whitespace and double spaces again as removing punctuation might
    # Lead to a white space
    article = article.apply(lambda x: re.sub(" +", " ", x))

    # Removing the Stopwords
    article = article.apply(
        lambda x: " ".join(word for word in x.split() if word not in stop_words)
    )

    return article


# Function to normalize the word frequency which is used in the function word_frequency
def normalize(li_word):
    global normalized_freq
    normalized_freq = []
    for dictionary in li_word:
        max_frequency = max(dictionary.values())
        for word in dictionary.keys():
            dictionary[word] = dictionary[word] / max_frequency
        normalized_freq.append(dictionary)
    return normalized_freq


# Function to calculate the word frequency
def word_frequency(article_word):
    word_frequency = {}
    li_word = []
    for sentence in article_word:
        for word in word_tokenize(sentence):
            if word not in word_frequency.keys():
                word_frequency[word] = 1
            else:
                word_frequency[word] += 1
        li_word.append(word_frequency)
        word_frequency = {}
    normalize(li_word)
    return normalized_freq


# Function to Score the sentence which is called in the function sent_token
def sentence_score(li):
    global sentence_score_list
    sentence_score = {}
    sentence_score_list = []
    for list_, dictionary in zip(li, normalized_freq):
        for sent in list_:
            for word in word_tokenize(sent):
                if word in dictionary.keys():
                    if sent not in sentence_score.keys():
                        sentence_score[sent] = dictionary[word]
                    else:
                        sentence_score[sent] += dictionary[word]
        sentence_score_list.append(sentence_score)
        sentence_score = {}
    return sentence_score_list


# Function to tokenize the sentence
def sent_token(article_sent):
    sentence_list = []
    sent_token = []
    for sent in article_sent:
        token = sent_tokenize(sent)
        for sentence in token:
            token_2 = "".join(word for word in sentence if word not in punctuation)
            token_2 = re.sub(" +", " ", token_2)
            sent_token.append(token_2)
        sentence_list.append(sent_token)
        sent_token = []
    sentence_score(sentence_list)
    return sentence_score_list


# Function which generates the summary of the articles (This uses the 20% of the sentences with the highest score)
def summary(sentence_score_OwO, percentage):
    summary_list = []
    for summ in sentence_score_OwO:
        select_length = int(len(summ) * percentage)
        summary_ = nlargest(select_length, summ, key=summ.get)
        summary_list.append(".".join(summary_))
    return summary_list


# Functions to change the article string (if passed) to change it to generate a pandas series
def make_series(art):
    global dataframe
    data_dict = {"article": [art]}
    dataframe = pd.DataFrame(data_dict)["article"]
    return dataframe


# Post process the text to do POS tagging and capitalize proper nouns
def postprocessing(summary: str) -> str:
    return capitalise_propn(summary)


# Function which is to be called to generate the summary which in further calls other functions alltogether
def summarize(artefact, percentage=0.05):

    if type(artefact) != pd.Series:
        artefact = make_series(artefact)

    df = preprocessing(artefact)

    word_normalization = word_frequency(df)

    sentence_score_OwO = sent_token(article_sent)

    summarized_article = summary(sentence_score_OwO, percentage)

    return postprocessing(summarized_article[0])
