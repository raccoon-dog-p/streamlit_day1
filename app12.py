import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import plotly.express as px

def main() :
    df1 = pd.read_csv('data/lang_data.csv')
    st.dataframe(df1)
    language_list=df1.columns[1:]
    choice_list = st.multiselect('데이터 프레임 컬럼 선택',language_list)
    if len(choice_list) != 0:
        # 유저가 선택한 컬럼만 차트를 그림
        selected_df = df1[choice_list]
        # 스트림릿이 제공하는 차트
        st.line_chart(selected_df)
        # 스트림릿이 제공하는 영역 차트
        st.area_chart(selected_df)
    df2= pd.read_csv('data/iris.csv')
    # 스트림 릿이 제공하는 바 차트
    st.bar_chart(df2[['sepal_length','petal_length']])

    # Altair 이용!
    # x 축과 y축 설정 + color 또는 size를 통하여 풍성하게 표현가능
    chart = alt.Chart(df2).mark_circle().encode(
        x = 'petal_length',
        y = 'petal_width',
        color = 'species'
    )
    st.altair_chart(chart)

    # 스트림릿의 map 차트
    df3 = pd.read_csv('data/location.csv',index_col=0)
    st.map(df3)

    # plotly를 이용한 차트 그리기
    df4 = pd.read_csv('data/prog_languages_data.csv',index_col=0)
    st.dataframe(df4)
    
    fig1= px.pie(df4,names='lang',values='Sum',title='각 언어별 파이차트')
    st.plotly_chart(fig1)

    # plotly의 bar 차트
    df4= df4.sort_values(by='Sum',ascending=False)
    fig2 = px.bar(df4,x='lang',y='Sum')
    st.plotly_chart(fig2)
if __name__ == '__main__':
    main()