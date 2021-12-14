import streamlit as st
import pandas as pd

def main():
    df = pd.read_csv('data/iris.csv')
    # if st.button('데이터 보기'):
    #     st.dataframe(df)
    # name = 'Mike'
    # if st.button('변환하기'):
    #     st.write(name.upper())
    # if st.button('소문자로 변환'):
    #     st.write(name.lower())

    species =df['species'].unique()
    if st.button('종류 확인'):
        st.write(species)


    status = st.radio('정렬을 선택하세요',['오름차순','내림차순'])
    if status == '오름차순':
        st.dataframe(df.sort_values('petal_length'))
    elif status == '내림차순':
        st.dataframe(df.sort_values('petal_length',ascending=False))
    
    
    language = ['Python','C','Go','Java']
    my_choice = st.selectbox('좋아하는 언어를 선택하세요',language)
    if my_choice == 'C':
        st.write ('저는 C가 좋아요')
    elif my_choice == 'Python':
        st.write('저는 Python이 좋아요')

    choice_list = st.multiselect('여러개를 선택할 수 있습니다.',language)
    #  여러분들이 디버깅을 하고 싶으면,
    #  python의 프린트 함수를 이용하면 아래의 터미널에 출력됨
    # print(choice_list)
    # column_list = st.multiselect('컬럼을 선택하세요',df.columns)
    # st.dataframe(df[column_list])
    # age = st.slider('나이선택',1,100,value=30)
    # st.write(f'선택한 나이는 {age}입니다.')
    
    with st.expander('hello') :
        st.text('안녕하세요')

if __name__ == '__main__':
    main()