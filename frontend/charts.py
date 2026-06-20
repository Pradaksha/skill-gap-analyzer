import streamlit as st

def show_match_score(score):

    st.progress(score / 100)