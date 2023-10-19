import time
import random as rand
import streamlit as st
import streamlit.components.v1 as components



# ====== Демонстрация некоторых функций Streamlit ===============

# можно записывать текст или markdown без st.write()

'''# :green[Добро пожаловать в великолепное приложение DaNetQA!!!!]'''
'''## Больше вам не придется самим искать ответ на вопрос в тонне текста. Достаточно только скопировать текст, задать вопрос, и мы дадим 100% верный ответ!'''

text = st.text_area('Просто вставь текст, в котором нужно искать ответ!')
question = st.text_input('А теперь введи свой вопрос, и я дам верный ответ!', disabled = not text)

def set_answer():
    st.write(question + " " + text)

st.button('Нажми на меня 3 раза', on_click=set_answer)









# то что будет введено в окошко запишется в text
text = st.text_area('Введите текст в окошко:')

# питоновский код который выполняется динамичски - печатает текст из окошка выше
st.code(f"""
import streamlit as st

st.write('Этот текст динамически печатается итерпретатором Python: {text}')
""")


# линия разделения - строка либо явно указать st.write('---')
st.write('---')

# ==================== Чекбокс =================

check_box = st.checkbox('Убери или поставь галку', value=True)
if check_box:
    st.write('**Вы поставили галку**')
elif not check_box:
    st.write('~~Вы убрали галку~~')


'---'
# ====================== Селект бокс ====================

choice_box = st.selectbox('Выберите вариант:', ['A', 'B', 'C'])
st.write(f'Вы выбрали {choice_box}')


'---'
# ======================= Переключатель ===================

choice_radio = st.radio('Выберите значение:', [1, 2, 3])
st.write(f'Вы выбрали {choice_radio}')


'---'
# ================ HTML код ============================
components.html('''
<p>
    <u>
        Это HTML Подчеркнутый текст
    </u>
</p>
<p>
    <font size=4 color='green'>
        Это зеленый HTML текст размера 4
    </font>
</p>
<p>
    <font color='A3A495'>
        <strong>
                Это серый жирный HTML текст
        </strong>
        <sup>
            это надстрочный текст
         </sup>
    </font>
</p>
''')


'---'
# =========== Счетчик нажатий кнопки =======================

# функция счетчик, вызывается при нажатии на кнопку
# st.session_state - состояние приложения, уникальное для каждого пользователя
# st.session_state поддерживает методы словаря
def image_detection_counter():
    # если нет атрибута detection_count в состоянии значит кнопка нажимается первый раз
    if 'detection_count' not in st.session_state:
        st.session_state.detection_count = 0
    # увеличиваем счетчик вызова функции на 1
    st.session_state.detection_count += 1


# ================== Кнопка =====================


# кнопка при нажатии на которую вызывается счетчик image_detection_counter
st.button('Нажми на меня 3 раза', on_click=image_detection_counter)

# если счетчик активирован и атрибут detection_count есть в состоянии приложения
if 'detection_count' in st.session_state:
    # показать счетчик нажатий на кнопку
    st.write(f'На меня нажали: {st.session_state.detection_count}')


# если нажали на кнопку 3 раза -
# st.session_state.get вернет значение атрибута если он есть или 0
if st.session_state.get('detection_count', 0) == 3:
    # окошко индикатора ожидания
    with st.spinner(text='Барабанная дробь ...'):
        time.sleep(3)
    # зеленое уведомление
    st.success('Задача выполнена!')

# если нажали кнопку больше 3х раз отображаем текст Markdown
elif st.session_state.get('detection_count', 0) > 3:
    st.write('## ***Вы нажали на кнопку более 3 раз***')

# если нажали кнопку менее 3х раз отображаем текст Markdown
else:
    st.write('### ***Вы нажали на кнопку менее 3 раз***')
