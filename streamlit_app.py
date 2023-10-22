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

import model_DaNetQA
import torch

# https://discuss.streamlit.io/t/adding-a-new-row-to-a-dataframe-with-each-button-click-persistent-dataframe/12799/3


# ====== Демонстрация некоторых функций Streamlit ===============

# можно записывать текст или markdown без st.write()

if 'answer_ready' not in st.session_state:
    st.session_state.answer_ready = False

if 'no_fields_qa' not in st.session_state:
    st.session_state.no_fields_qa = 2

'''# :green[Добро пожаловать в великолепное приложение DaNetQA!!!!]'''
'''## Больше вам не придется самим искать ответ на вопрос в тонне текста. Достаточно только скопировать текст, задать вопрос, и мы дадим 100% верный ответ!'''

text = st.text_area('Просто вставь текст, в котором нужно искать ответ!')
question = st.text_input('А теперь введи свой вопрос, и я дам верный ответ!', disabled = not text)

def set_answer():
  if text and question:
    st.write("## Секунду, готовлю ответ!")
    st.session_state.no_fields_qa = 1
    st.session_state.answer_ready = True
  else:
    st.session_state.no_fields_qa = 0
    st.session_state.answer_ready = False

def set_answer_df():
  pass

st.button('Получи ответ!', on_click=set_answer)

if st.session_state.no_fields_qa == 0:
  st.write("### Для получения результата нужно ввести и текст, и вопрос!")

if st.session_state.answer_ready == True:
    result = model_DaNetQA.model_answer([question],[text])
    st.write(result)
    for i in result:
      if i:
        st.write("# Да!")
      else:
        st.write("# Нет!")

if 'df' not in st.session_state:
  st.session_state.df = pd.DataFrame(columns = ["Текст","Вопрос", "Ответ"])

if st.button("Добавить новую строку"):
    st.session_state.df.loc[len(st.session_state.df.index)] = ["", "", ""]

st.dataframe(st.session_state.df) 


st.button('Получи ответ на множество вопросов!', on_click=set_answer_df)




