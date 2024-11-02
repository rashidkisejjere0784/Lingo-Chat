import streamlit as st
from streamlit_chat import message
from sqlalchemy.sql import text
from streamlit.components.v1 import html
from streamlit_autorefresh import st_autorefresh
from utils import language_maplet
from utils.translator import translate_text
from utils.sql_injection_filter import filter_sql_injection



if "view_chat" not in st.session_state:
    st.session_state['message'] = "Select a chat first"
    st.switch_page("pages/chat.py")

if "language" not in st.session_state:
    selected_language = "english"
else:
    selected_language = st.session_state['language']

partner_name = st.session_state['partner_name']
user_id = st.session_state['user id']
name = st.session_state['name']
email = st.session_state['email']
table_name = st.session_state['table_name']

count = st_autorefresh(interval=2000, limit=None, key="fizzbuzzcounter")

conn = st.connection("mysql", type="sql")

with conn.session as s:
    results = s.execute(
        text(f"SELECT * FROM {table_name}")
    )
    results = results.fetchall()
    s.commit()

def on_send_clicked(user_input):
    user_input = filter_sql_injection(user_input)   
    with conn.session as s:
        s.execute(
            text(f"INSERT INTO {table_name} (sender_id, content, src_lang) VALUES ({user_id}, '{user_input}', '{language_maplet.language_maplet[selected_language]}')")
        )
        s.commit()

def on_back_click():
    del(st.session_state['view_chat'])
    del(st.session_state['language'])
    st.rerun()

#st.title(f"Chat Between Me And {partner_name}")

st.markdown(
    f"""
    <div style="text-align: center; padding: 1rem;">
        <h1 style="color: #10B981; font-size: 2.5rem; font-weight: bold;">
            Chat Between Me And {partner_name}
        </h1>
    </div>
    """,
    unsafe_allow_html=True
)


chat_placeholder = st.empty()

with chat_placeholder.container():    
    for result in results:
        if(result[3] != selected_language):
            translated_text = translate_text(
                result[2], src=result[3], dest=language_maplet.language_maplet[selected_language]
            )
            
        if result[1] == user_id:
            message(translated_text, is_user=True, key=result[0])
        else:
            message(translated_text, key=result[0])
    
    st.button("Back", on_click=on_back_click)

col1, col2 = st.columns(2)

with col1:
    user_input = st.text_input("User Input:")

with col2:
    option = st.selectbox(
        "Select Language",
        language_maplet.language_maplet.keys(),
        index=27,
        placeholder="Select Language",
    )

    st.write('You selected:', option)
    st.session_state['language'] = option
    st.button("send", on_click=on_send_clicked, args=[user_input])
