from deep_translator import GoogleTranslator
import streamlit as st

@st.cache_data
def translate_text(text : str, src: str, dest: str) -> str:
    translation = GoogleTranslator(source=src, target=dest).translate(text)
    return translation