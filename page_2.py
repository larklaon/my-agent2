import pandas as pd
import streamlit as st


def preview_excel(uploaded_file):
    try:
        table = pd.read_excel(uploaded_file)
    except Exception:
        st.error(f"{uploaded_file.name}을(를) 읽을 수 없습니다. 엑셀 파일 형식을 확인해 주세요.")
        return

    st.text(uploaded_file.name)
    st.dataframe(table)


st.title("엑셀 미리보기")

mode = st.radio("업로드 방식", ["단일 파일", "복수 파일"], horizontal=True)
if mode == "단일 파일":
    uploaded_file = st.file_uploader(
        "엑셀 파일을 선택하세요", type=["xlsx", "xls"], key="single_excel"
    )
    if uploaded_file is not None:
        preview_excel(uploaded_file)
else:
    uploaded_files = st.file_uploader(
        "엑셀 파일을 선택하세요",
        type=["xlsx", "xls"],
        accept_multiple_files=True,
        key="multiple_excel",
    )
    for uploaded_file in uploaded_files:
        preview_excel(uploaded_file)
