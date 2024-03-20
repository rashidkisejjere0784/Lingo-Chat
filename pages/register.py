import streamlit as st
from sqlalchemy.sql import text

st.title("Register into Lingo Chat")

name = st.text_input("Enter your Name")
email = st.text_input("Enter your Email")
password = st.text_input("Enter your password", type='password')
confirm_password = st.text_input("Confirm password", type='password')
submit = st.button("Register")

def validateInput(field, label):
    if not field:
        st.error(f"{label} is required")

if submit:
    validateInput(name, "Name")
    validateInput(email, "Email")
    validateInput(password, "Password")
    validateInput(confirm_password, "Confirm Password")
    
    if password != confirm_password:
        st.error("Password mismatch")
    else:
        conn = st.connection('mysql', type='sql')
        with conn.session as s:
            result = s.execute(
                text(f"INSERT INTO users (name, email, password) VALUES ('{name}', '{email}', '{password}');")
            )
            
            s.commit()
            
        st.success("Registration successful!")
        st.session_state['user id'] = result.lastrowid
        st.session_state['name'] = name
        st.session_state['email'] = email
        
        st.switch_page("pages/chat.py")
