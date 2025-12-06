import streamlit as st
from textblob import TextBlob

st.title("Simple Spell Checker")

text = st.text_area("Enter Text:")

if st.button("Correct"):
    if text:
        blob = TextBlob(text)
        corrected_text = blob.correct()
        st.write("**Corrected Text:**", corrected_text)