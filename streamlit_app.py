import time
import random as rand
import streamlit as st
import streamlit.components.v1 as components
import pickle
import re
import string
from pymorphy2 import MorphAnalyzer
import nltk
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

import model_DaNetQA
import torch

def get_result_from_model(question, text):
    answer = 1
    if answer == 1:
        return "YES"
    else:
        return "NO"

# https://discuss.streamlit.io/t/adding-a-new-row-to-a-dataframe-with-each-button-click-persistent-dataframe/12799/3


# ====== Демонстрация некоторых функций Streamlit ===============

# можно записывать текст или markdown без st.write()

if 'answer_ready' not in st.session_state:
    st.session_state.answer_ready = False
if 'no_fields' not in st.session_state:
    st.session_state.no_fields = 2

'''# :green[Добро пожаловать в великолепное приложение DaNetQA!!!!]'''
'''## Больше вам не придется самим искать ответ на вопрос в тонне текста. Достаточно только скопировать текст, задать вопрос, и мы дадим 100% верный ответ!'''

text = st.text_area('Просто вставь текст, в котором нужно искать ответ!')
question = st.text_input('А теперь введи свой вопрос, и я дам верный ответ!', disabled = not text)

def set_answer():
  if text and question:
    st.write(st.session_state.answer_ready)
  else:
    st.session_state.no_fields

st.button('Получи ответ!', on_click=set_answer)
if st.session_state.no_fields == 0:
  st.write("### Для получения результата нужно ввести и текст, и вопрос!")

if st.session_state.answer_ready == True:
    result = model_DaNetQA.model_answer([question],[text])
    for i in result:
      if i:
        st.write("# Да!")
      else:
        st.write("# Нет!")







