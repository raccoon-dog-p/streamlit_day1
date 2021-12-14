import streamlit as st
# 다른 파일에서 연동
from eda_app import run_eda_app
from ml_app import run_ml_app
def main():
    st.title('파일 분리 앱')
    menu =['Home','Eda','ML','About']
    choice=st.sidebar.selectbox("메뉴",menu)
    
    if choice == 'Home':
        st.subheader('홈입니다')
    elif choice == 'Eda':
        run_eda_app()

    elif choice == 'ML':
        run_ml_app()
    
    else:
        st.subheader('앱 소개 화면입니다.')

if __name__ == '__main__':
    main()