import streamlit as st

def main():
    st.title('HELLO WORLD')
    st.text('웹 대시보드 프로젝트')
    name = '홍길동'
    st.text(f'제 이름은 {name} 입니다.')
    st.header('이 영역은 헤더영역')
    st.subheader('이 영역은 서브헤더 영역')
    st.success('성공')
    st.warning('경고')
    st.info('정보 영역 ')
    st.error('이건 에러')
    st.help(range)
    st.help(sum)
if __name__ == '__main__':
    main()
