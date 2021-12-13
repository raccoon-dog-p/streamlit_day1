#pip install streamlit 은 이미 설치함

import streamlit as st

# 웹 대시보드 개발 라이브러리인 스트림릿은 
# main 함수가 있어야 한다.
# streamlit 실행은 command prompt에서 streamlit run 파일명.py
# 서버 중지를 원할시 터미널 내부에서 ctr + c
def main():
    st.title('Hello Streamlit, 안녕하세요')

if __name__ == '__main__' :
    main()
