import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np

def main():
    st.title('Plotting with st.pyplot()')

    df = pd.read_csv('data/iris.csv')

    st.dataframe(df.head())

    # 차트 그리기
    # sepal_length와 sepal_width 관계 그리기
    fig = plt.figure()
    plt.scatter(data= df,x='sepal_length',y='sepal_width')
    plt.title ('sepal corr')
    plt.xlabel('sepal length')
    plt.ylabel('sepal width')
    st.pyplot(fig)
    st.dataframe(df.corr())

    fig2 = plt.figure()
    sb.regplot(data=df,x='sepal_length',y='sepal_width')
    st.pyplot(fig2)

    fig3 = plt.figure()
    sb.histplot(data=df,x='sepal_length',bins=20)
    st.pyplot(fig3)

    # species 에는 종 정보가 들어있다.
    # 각 종별로 몇개씩 있는지를 차트로 나타내라
    fig4 = plt.figure()
    sb.countplot(x = df['species'])
    st.pyplot(fig4)

    # 데이터 프레임의 차트 그리는것도 가능
    fig5 = plt.figure()
    df['species'].value_counts().plot(kind='bar')
    st.pyplot(fig5)

    fig6= plt.figure()
    df['sepal_length'].hist()
    st.pyplot(fig6)
if __name__ == '__main__':
    main()