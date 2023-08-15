import streamlit as st
import csv

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=500)

with col2:
    st.title("Bastian Hörger")
    selfdescription = """
    This is a placeholder for text about me!
    """
    st.info(selfdescription)