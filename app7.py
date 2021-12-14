import streamlit as st
from PIL import Image

def main():
    image = Image.open('data/image_03.jpg')
    st.set_page_config(page_title='Machine Learning',
    page_icon=image,layout='wide',initial_sidebar_state='collapsed')
if __name__ == '__main__':
    main()