import time
import random as rand
import streamlit as st
import streamlit.components.v1 as components
import pickle
import re
import string
from pymorphy2 import MorphAnalyzer
import nltk
import pandas as pd
import numpy as np
from gensim.models import KeyedVectors
from nltk.tokenize import word_tokenize
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, confusion_matrix,
                             ConfusionMatrixDisplay, precision_score,
                             recall_score)
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn.neighbors import KNeighborsClassifier
import torch

def tokens_creator(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub("\s+", " ", text)
    text = text.strip()

    tokens = word_tokenize(text)

    return tokens

def morph_transform(tokens, analyzer, model):
    keys = []
    for token in tokens:
        parsed = morph.parse(token)
        if len(parsed) == 0:
            continue
        nf = parsed[0].normal_form
        pos = parsed[0].tag.POS
        key = f"{nf}_{pos}"
        keys.append(key)

    vector = pd.Series(model.get_mean_vector(keys))

    return vector


def model_answer(question, passage):
  morph = MorphAnalyzer()
  loaded_model = pickle.load(open("CLF model.sav", 'rb'))
  curr = pd.DataFrame(list(zip(question, passage)), columns=["question","passage"])
  
  curr["text"] = curr["question"] + " " + curr["passage"]
  curr["text"]
  
  
  curr["question_tokens"] = curr["question"].apply(tokens_creator)
  curr["passage_tokens"] = curr["passage"].apply(tokens_creator)
  curr["text_tokens"] = curr["question_tokens"] + curr["passage_tokens"]
  curr["text_tokens"]
  
  curr_X_q = curr["question_tokens"].apply(lambda x: morph_transform(x, morph, pretrained_model)).to_numpy()
  curr_X_p = curr["passage_tokens"].apply(lambda x: morph_transform(x, morph, pretrained_model)).to_numpy()
  curr_X = np.concatenate((curr_X_q, curr_X_p), axis=1)
  
  loaded_model_y_pred = loaded_model.predict(curr_X)
  return loaded_model_y_pred
