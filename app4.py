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
if __name__ == '__main__':
    main()