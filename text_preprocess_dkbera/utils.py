import re
import os
import sys

import pandas as pd
import numpy as np
import spacy
from spacy.lang.en.stop_words import STOP_WORDS as stopwords
from bs4 import BeautifulSoup
import unicodedata
from textblob import TextBlob

nlp=spacy.load('en_core_web_lg')

def _get_wordcounts(x):
	length = len(str(x).split())
	return length

def _get_charcounts(x):
	s=x.split()
	x="".join(s)
	return len(x)

def _get_avg_wordlength(x):
	count=_get_charcounts(x)/_get_wordcounts(x)
	return count

def _get_stopword_counts(x):
	l = len([t for t in x.split() if t in stopwords])
	return l

def _get_hastag_counts(x):
	hastag_len = len([t for t in x.split() if t.startswith('#')])
	return hastag_len

def _get_mention_counts(x):
	mention_count = len([t for t in text.split() if t.startswith('@')])
	return mention_count

def _get_degit_counts(x):
	digit_count=len([t for t in x.split() if t.isdigit()])
	return digit_count

def _get_uppercase_counts(x):
	return len([t for t in x.split() if t.isupper()])

def _cont_exp(x):
	cList = {
	"ain't": "am not",
	"aren't": "are not",
	"can't": "cannot",
	"can't've": "cannot have",
	"'cause": "because",
	"could've": "could have",
	"couldn't": "could not",
	"couldn't've": "could not have",
	"didn't": "did not",
	"doesn't": "does not",
	"don't": "do not",
	"hadn't": "had not",
	"hadn't've": "had not have",
	"hasn't": "has not",
	"haven't": "have not",
	"he'd": "he would",
	"he'd've": "he would have",
	"he'll": "he will",
	"he'll've": "he will have",
	"he's": "he is",
	"how'd": "how did",
	"how'd'y": "how do you",
	"how'll": "how will",
	"how's": "how is",
	"I'd": "I would",
	"I'd've": "I would have",
	"I'll": "I will",
	"I'll've": "I will have",
	"I'm": "I am",
	"I've": "I have",
	"i'd": "I would",
	"i'd've": "I would have",
	"i'll": "I will",
	"i'll've": "I will have",
	"i'm": "I am",
	"i've": "I have",
	"isn't": "is not",
	"it'd": "it had",
	"it'd've": "it would have",
	"it'll": "it will",
	"it'll've": "it will have",
	"it's": "it is",
	"let's": "let us",
	"ma'am": "madam",
	"mayn't": "may not",
	"might've": "might have",
	"mightn't": "might not",
	"mightn't've": "might not have",
	"must've": "must have",
	"mustn't": "must not",
	"mustn't've": "must not have",
	"needn't": "need not",
	"needn't've": "need not have",
	"o'clock": "of the clock",
	"oughtn't": "ought not",
	"oughtn't've": "ought not have",
	"shan't": "shall not",
	"sha'n't": "shall not",
	"shan't've": "shall not have",
	"she'd": "she would",
	"she'd've": "she would have",
	"she'll": "she will",
	"she'll've": "she will have",
	"she's": "she is",
	"should've": "should have",
	"shouldn't": "should not",
	"shouldn't've": "should not have",
	"so've": "so have",
	"so's": "so is",
	"that'd": "that would",
	"that'd've": "that would have",
	"that's": "that is",
	"there'd": "there had",
	"there'd've": "there would have",
	"there's": "there is",
	"they'd": "they would",
	"they'd've": "they would have",
	"they'll": "they will",
	"they'll've": "they will have",
	"they're": "they are",
	"they've": "they have",
	"to've": "to have",
	"wasn't": "was not",
	"we'd": "we had",
	"we'd've": "we would have",
	"we'll": "we will",
	"we'll've": "we will have",
	"we're": "we are",
	"we've": "we have",
	"weren't": "were not",
	"what'll": "what will",
	"what'll've": "what will have",
	"what're": "what are",
	"what's": "what is",
	"what've": "what have",
	"when's": "when is",
	"when've": "when have",
	"where'd": "where did",
	"where's": "where is",
	"where've": "where have",
	"who'll": "who will",
	"who'll've": "who will have",
	"who's": "who is",
	"who've": "who have",
	"why's": "why is",
	"why've": "why have",
	"will've": "will have",
	"won't": "will not",
	"won't've": "will not have",
	"would've": "would have",
	"wouldn't": "would not",
	"wouldn't've": "would not have",
	"y'all": "you all",
	"y'alls": "you alls",
	"y'all'd": "you all would",
	"y'all'd've": "you all would have",
	"y'all're": "you all are",
	"y'all've": "you all have",
	"you'd": "you had",
	"you'd've": "you would have",
	"you'll": "you you will",
	"you'll've": "you you will have",
	"you're": "you are",
	"you've": "you have",
	"bak":"back",
	"dis":"this",
	"brng":"bring"
	}
	if type(x) is str:
		for key in cList:
			value=cList[key]
			x=x.replace(key, value)
		return x
	else:
		return x

def _get_emails(x):
	emails=re.findall(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+._-]+)',x)
	count=len(emails)
	return emails, count

def _remove_emails(x):
	text = re.sub(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+._-]+)',"",x)
	return text

def _get_urls(x):
	url=re.findall(r"(?i)\b(?:ftp|https?|ssh)://(?:[a-zA-Z]|[0-9]|[$~#-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", x)
	count=len(url)
	return url, count

def _remove_urls(x):
	t=re.sub(r"(?i)\b(?:ftp|https?|ssh)://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", "",x)
	return t

def _remove_rt(x):
	return re.sub(r'\brt\b','',x).strip()

def _remove_special_chars(x):
	x=re.sub(r"[^\w ]+","",x)
	x=" ".join(x.split())
	return x

def _remove_html_tags(x):
	return BeautifulSoup(x, "lxml").get_text().strip()

def _remove_accented_chars(x):
	x=unicodedata.normalize("NFKD", x).encode("ASCII", "ignore").decode("utf-8", "ignore")
	return x

def _remove_stopwords(x):
	x=" ".join(x for x in text.split() if x not in stopwords)
	return x

def _make_base(x):
	x=str(x)
	doc=nlp(x)
	x_list=[]
	for token in doc:
		lem=token.lemma_
		if lem=="-PRON" or lem == "be":
			lem=token.text
		x_list.append(lem)
	return " ".join(x_list)

def _get_value_counts(df, col):
	text = " ".join(df[col])
	text=text.split()
	comm_word=pd.Series(text).value_counts()
	return comm_word

def _remove_common_words(x, comm_word, n=20):
	fq=comm_word[:n]
	x = " ".join([t for t in x.split() if t not in fq])
	return x

def _remove_rare_words(x, comm_word,n=20):
	fq=comm_word.tail(n)
	x = " ".join([t for t in x.split() if t not in fq])
	return x

def _spell_correction(x):
	x=TextBlob(x).correct()
	return x
