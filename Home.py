import streamlit as st
from streamlit_chat import message, AvatarStyle

conn = st.connection('mysql', type='sql')


st.title("Welcome to Lingo Chat")

st.write("cool")