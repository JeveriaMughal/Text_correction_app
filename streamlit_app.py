import streamlit as st
import stapp1,stapp2

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")
PAGES = {"تصویر سے اردو تحریر": stapp1,
        "اصلاح":stapp2}
st.sidebar.title("NLP-L \n Text extraction and correction module")
st.sidebar.image("logo-white_old.png")
selection = st.sidebar.radio("صفحہ",list (PAGES.keys()))
page= PAGES[selection]
page.app()