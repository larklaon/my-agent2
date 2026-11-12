import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Streamlit 실습")

page = st.navigation(
    [
        st.Page("page_1.py", title="챗봇", icon="1️⃣"),
        st.Page("page_2.py", title="엑셀 미리보기", icon="2️⃣"),
        st.Page("page_3.py", title="환율 조회", icon="3️⃣"),
    ],
    position="top",
)
page.run()
