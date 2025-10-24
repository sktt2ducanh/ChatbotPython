import streamlit as st

st.title("web sex")

name = st.text_input("Tai khoan")
pass2 = st.text_input("Mat Khau")
if st.button("Dang nhap"):
    if name == "ducanh" and pass2 == "123456":
        st.success("Dang nhap thanh cong")
    else:
        st.error("Sai tk mk")