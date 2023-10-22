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

st.write("## ")
st.write("## ")
st.write("## А если хочешь задать сразу много вопросов, можешь воспользоваться формой ниже, а далее, нужно всего нажать на одну кнопку - и готово!")
data = st.experimental_data_editor(pd.DataFrame(columns = ["Текст","Вопрос"]),num_rows="dynamic")
if 'df' not in st.session_state:
  st.session_state.df = data
st.session_state.df = data
if st.button('Получи ответ на множество вопросов!'):
  result = model_DaNetQA.model_answer(st.session_state.df["Вопрос"].tolist(), st.session_state.df["Текст"].tolist())
  true_res = []
  for i in result:
    if i:
      true_res.append("Да!")
    else:
      true_res.append("Нет!")
  st.write("## Держи ответы на все твои вопросы!")
  st.write(pd.DataFrame(list(zip(st.session_state.df["Вопрос"].tolist(), true_res)), columns=["Вопрос","Ответ"]))

