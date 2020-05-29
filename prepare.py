import unicodedata
import re # for replacing non-alphanumeric characters, etc
import json

from requests import get
from bs4 import BeautifulSoup
import os

# natural language toolkit
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

import pandas as pd
import numpy as np

import acquire

string = ""

# function to quickly clean up article data:
def basic_clean(string):
    """
    Function take a string, lowercase it, normalize it, and remove all non-ASCII characters
    """
    
    # to lowercase all the text:
    string = string.lower()
    string = unicodedata.normalize('NFKD', string)\
    .encode('ascii', 'ignore')\
    .decode('utf-8', 'ignore') 
    
    # to remove anything that is not a letter, number, whitespace, or single-quote:
    string = re.sub(r"[^a-zA-Z0-9'\s]", '', string)

    return string

# function to tokenize text
def tokenize(string):
    """
    Function to take in a string and break it down into discrete parts
    """
    
    # to lowercase all the text:
    string = string.lower()
    string = unicodedata.normalize('NFKD', string)\
    .encode('ascii', 'ignore')\
    .decode('utf-8', 'ignore') 
    
    # to remove anything that is not a letter, number, whitespace, or single-quote:
    string = re.sub(r"[^a-zA-Z0-9'\s]", '', string)

    # applying the tokenizer object
    tokenizer = nltk.tokenize.ToktokTokenizer()
    string = tokenizer.tokenize(string, return_str=True)
    
    return string

# function to stem all the text - only stem on huge datasets

def stem(string):
    """
    Function that takes in text and stems all the words down into their base forms
    """
    
    # to lowercase all the text:
    string = string.lower()
    string = unicodedata.normalize('NFKD', string)\
    .encode('ascii', 'ignore')\
    .decode('utf-8', 'ignore') 
    
    # to remove anything that is not a letter, number, whitespace, or single-quote:
    string = re.sub(r"[^a-zA-Z0-9'\s]", '', string)
    
    # applying the tokenizer object
    tokenizer = nltk.tokenize.ToktokTokenizer()
    string = tokenizer.tokenize(string, return_str=True)
    
    # stemming everything
    ps = nltk.porter.PorterStemmer()
    words = [string]
    stems = [ps.stem(word) for word in string.split()]
    string_stemmed = ' '.join(stems)

    return string_stemmed

# Function to lemmatize the text - Lemmatization is much cleaner than stemming but takes more computational power

def lemmatize(text):
    """
    Function that takes in text and stems all the words down into their base forms
    """
    
    # to lowercase all the text:
    text = text.lower()
    text = unicodedata.normalize('NFKD', text)\
    .encode('ascii', 'ignore')\
    .decode('utf-8', 'ignore') 
    
    # to remove anything that is not a letter, number, whitespace, or single-quote:
    text = re.sub(r"[^a-zA-Z0-9'\s]", '', text)
    
    # applying the tokenizer object
    tokenizer = nltk.tokenize.ToktokTokenizer()
    text = tokenizer.tokenize(text, return_str=True)
    
    # lemmatizing everything
    wnl = nltk.stem.WordNetLemmatizer()
    lemmas = [wnl.lemmatize(word) for word in text.split()]
    text_lemmatized = ' '.join(lemmas)

    return text_lemmatized

# Function to remove all the english stopwords from the text, with options to add / remove stopwords:

def remove_stopwords(text, extra_words="", exclude_words=""):
    """
    Function that takes in text and stems all the words down into their base forms
    """
    
    # to lowercase all the text:
    text = text.lower()
    text = unicodedata.normalize('NFKD', text)\
    .encode('ascii', 'ignore')\
    .decode('utf-8', 'ignore') 
    
    # to remove anything that is not a letter, number, whitespace, or single-quote:
    text = re.sub(r"[^a-zA-Z0-9'\s]", '', text)
    
    # applying the tokenizer object
    tokenizer = nltk.tokenize.ToktokTokenizer()
    text = tokenizer.tokenize(text, return_str=True)
    
    # lemmatizing everything
    wnl = nltk.stem.WordNetLemmatizer()
    lemmas = [wnl.lemmatize(word) for word in text.split()]
    text_lemmatized = ' '.join(lemmas)

    # removing stopwords
    words = text.split()
    filtered_words = [w for w in words if w not in stopword_list]
    print("removed {} stopwords".format(len(words) - len(filtered_words)))
    print("***************")
    text_without_stopwords = ' '.join(filtered_words)
    
    return text_without_stopwords