import streamlit as st
import pandas as pd
# 이미지 처리를 위한 라이브러니
from PIL import Image

def main():
    img = Image.open('data/image_03.jpg')
    print(img)
    st.image(img)
    # st.image(img,use_column_width=True)
    st.image('https://www.outdoornews.co.kr/news/photo/202009/32077_90504_551.jpg')
    video_file = open('data/dog.mp4.mp4','rb')
    st.video(video_file)
    # audio_file = opem('data/song.mp3)
    # st.audio(audio_file.read(),format='audio/mp3')
if __name__ == '__main__':
    main()