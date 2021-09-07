from heapq import nlargest

import pandas as pd
import numpy as np
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


# # Function to clean the html from the article
# def cleanhtml(raw_html):
#     cleanr = re.compile('<.*?>')
#     cleantext = re.sub(cleanr, '', raw_html)
#     return cleantext

# # Function expand the contractions if there's any


# def expand_contractions(s, contractions_dict=contractions_dict):
#     def replace(match):
#         return contractions_dict[match.group(0)]
#     return contractions_re.sub(replace, s)


# # Function to preprocess the articles
# def preprocessing(article):
#     global article_sent

#     # Converting to lowercase
#     article = article.str.lower()

#     # Removing the HTML
#     article = article.apply(lambda x: cleanhtml(x))

#     # Removing the email ids
#     article = article.apply(lambda x: re.sub('\S+@\S+', '', x))

#     # Removing The URLS
#     article = article.apply(lambda x: re.sub(
#         "((http\://|https\://|ftp\://)|(www.))+(([a-zA-Z0-9\.-]+\.[a-zA-Z]{2,4})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(/[a-zA-Z0-9%:/-_\?\.'~]*)?", '', x))

#     # Removing the '\xa0'
#     article = article.apply(lambda x: x.replace("\xa0", " "))

#     # Removing the contractions
#     article = article.apply(lambda x: expand_contractions(x))

#     # Stripping the possessives
#     article = article.apply(lambda x: x.replace("'s", ''))
#     article = article.apply(lambda x: x.replace('’s', ''))
#     article = article.apply(lambda x: x.replace("\'s", ''))
#     article = article.apply(lambda x: x.replace("\’s", ''))

#     # Removing the Trailing and leading whitespace and double spaces
#     article = article.apply(lambda x: re.sub(' +', ' ', x))

#     # Copying the article for the sentence tokenization
#     article_sent = article.copy()

#     # Removing punctuations from the article
#     article = article.apply(lambda x: ''.join(
#         word for word in x if word not in punctuation))

#     # Removing the Trailing and leading whitespace and double spaces again as removing punctuation might
#     # Lead to a white space
#     article = article.apply(lambda x: re.sub(' +', ' ', x))

#     # Removing the Stopwords
#     article = article.apply(lambda x: ' '.join(
#         word for word in x.split() if word not in stop_words))

#     return article


# # To normalize word frequency in the word frequency list
# def normalize(word_freq_list):
#     normalized_freq = []

#     for dictionary in word_freq_list:
#         # Calculate the max frequency of a particular dictionary
#         max_freq = max(dictionary.values())

#         # For each word in the dictionary, normalize its frequency
#         for word in dictionary.keys():
#             dictionary[word] = dictionary[word] / max_freq

#         # Add the normalized dictionary to the list
#         normalized_freq.append(dictionary)

#     return normalized_freq


# # To calculate the word frequency
# def word_frequency(article_word):
#     word_freq = {}
#     word_freq_list = []

#     # For each sentence in the article
#     for sentence in article_word:
#         for word in word_tokenize(sentence):
#             if word not in word_freq.keys():
#                 # Add the word to the dictionary if not exists
#                 word_freq[word] = 1
#             else:
#                 # Increment the word's frequency if exists
#                 word_freq[word] += 1

#         # Append the frequency dictionary to the list
#         word_freq_list.append(word_freq)

#         # Make the word_freq empty for next sentence
#         word_freq = {}

#     normalized_freq = normalize(word_freq_list)
#     return normalized_freq


# # To score a sentence which used during sentence tokenization
# def sentence_score(li, normalized_freq):
#     sentence_score = {}
#     sentence_score_list = []

#     for _list, dictionary in zip(li, normalized_freq):
#         for sentence in _list:
#             for word in word_tokenize(sentence):
#                 if word in dictionary.keys():
#                     if sentence not in sentence_score.keys():
#                         sentence_score[sentence] = dictionary[word]
#                     else:
#                         sentence_score[sentence] += dictionary[word]

#         sentence_score_list.append(sentence_score)
#         sentence_score = {}

#     return sentence_score_list


# # To tokenize a sentence
# def sentence_token(ariticle_sentences, normalized_freq: List[dict]):
#     sentence_list = []
#     sentence_token = []

#     for sent in ariticle_sentences:
#         token = sent_tokenize(sent)

#         for sentence in token:
#             token_2 = ''.join(
#                 word for word in sentence if word not in punctuation)
#             token_2 = re.sub(' +', ' ', token_2)
#             sentence_token.append(token_2)

#         sentence_list.append(sentence_token)
#         sentence_token = []

#     sentence_score_list = sentence_score(sentence_list, normalized_freq)

#     return sentence_score_list


# # To generate the summary of an the articles
# # (This uses `percentage` of the sentences with the highest score)
# def summary(sentence_score, percentage):
#     summary_list = []

#     for summ in sentence_score:
#         select_length = int(len(summ) * percentage)
#         summary = nlargest(select_length, summ, key=summ.get)
#         summary_list.append(".".join(summary))

#     return summary_list


# # Convert the text string to pandas series
# def make_series(text):
#     data_dict = {'text': [text]}
#     dataframe = pd.DataFrame(data_dict)['text']
#     return dataframe

# # To generate the summary which in further calls other functions altogether


# def summarize(artefact, percentage):
#     if type(artefact) != pd.Series:
#         artefact = make_series(artefact)

#     df = preprocessing(artefact)

#     word_normalization = word_frequency(df)

#     print("Word Normlization:")
#     print(word_normalization)
#     print()

#     sentence_score = sentence_token(df, word_normalization)

#     print("Sentence Score:")
#     print(sentence_score)
#     print()

#     summarized_article = summary(sentence_score, percentage)

#     print("Summarized Article:")
#     print(summarized_article)
#     print()

#     return summarized_article

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
