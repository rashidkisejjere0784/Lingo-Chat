import streamlit as st
from sqlalchemy.sql import text


conn = st.connection("mysql", type='sql')

if 'message' in st.session_state:
    st.warning(st.session_state['message'])
    del(st.session_state['message'])

if 'user id' not in st.session_state:
    st.session_state['message'] = "Not Logged In"
    st.switch_page("pages/login.py")
    
user_id = st.session_state['user id']
name = st.session_state['name']
email = st.session_state['email']

if "view_chat" in st.session_state:
    st.switch_page('pages/view_chat.py')

st.markdown(f"""<h1 style='text-align: center ; color: #10B981 ; font-size: 2.5rem; font-weight: bold;'>Hi {name}, Select someone to chat with:</h1>""", unsafe_allow_html=True)

with conn.session as s:
    all_chats = s.execute(
        text(f"SELECT id, name FROM users WHERE id != {user_id}")
    )
    
    s.commit()

def on_input_change():
    user_input = st.session_state.user_input
    st.session_state.past.append(user_input)
    st.session_state.generated.append("The messages from Bot\nWith new line")

def on_btn_click():
    del st.session_state.past[:]
    del st.session_state.generated[:]


def display_chat(partner_id, partner_name):
    # Create the messages table if it doesn't exist
    data_order = (user_id, partner_id) if user_id < partner_id else (partner_id, user_id)
    
    create_table_query = f"""
                            CREATE TABLE IF NOT EXISTS messages_{data_order[0]}_{data_order[1]} (
                                id INT AUTO_INCREMENT PRIMARY KEY,
                                sender_id INT(255),
                                content TEXT,
                                src_lang VARCHAR(10),
                                timestamp TIMESTAMP DEFAULT NOW()
                            );
                        """
    
    with conn.session as s:
        s.execute(text(create_table_query))

        s.commit()
    
    st.session_state['view_chat'] = True
    st.session_state['partner_id'] = partner_id
    st.session_state['partner_name'] = partner_name
    st.session_state['table_name'] = f"messages_{data_order[0]}_{data_order[1]}"
    
    st.experimental_rerun()
   
# Display the list of available chat partners in a scrollable container
partners = st.expander("Available Partners:", expanded=False)
with partners:
    cols = st.columns([2, 1])
    for row in all_chats:
        partner_id, partner_name = row
        cols[0].markdown(f"**{partner_name}**")
        cols[1].button(f"Chat ({partner_name})", key=partner_id, on_click=display_chat, args=(partner_id, partner_name))