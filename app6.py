from google.protobuf import message
import streamlit as st

# 유저한테 입력받는 방법
def main():
    name = st.text_input('이름을 입력하세요')
    st.write(name)

    name2 = st.text_input('이름을 입력하세요',max_chars=5)
    st.write(name2)

    message = st.text_area('메세지를 입력하세요',height=3)
    st.text(message)

    num = st.number_input('숫자 입력하세요',1,100)
    st.text(num)

    num2 = st.number_input('숫자 입력하세요',0.0,100.0)
    st.text(num2)

    # 날짜
    my_date = st.date_input('약속날짜를 입력하세요')
    st.write(my_date)

    # 디버깅을 원하면 print(my_date)

    # 시간
    my_time = st.time_input('시간 선택')
    st.write(my_time)

    # 비밀번호 입력
    password = st.text_input('비밀번호 입력',type='password',max_chars=12)
    st.write(password)

    # 색깔 입력
    color = st.color_picker('컬러 입력')
    st.write(color)
    
if __name__ == '__main__':
    main()