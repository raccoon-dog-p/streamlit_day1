# 여러 파일을 업로드 하는 앱

import streamlit as st
from PIL import Image
import pandas as pd
import os
from datetime import datetime
from streamlit.uploaded_file_manager import UploadedFile

def save_uploaded_file(directory, file) :
    # 1.디렉토리가 있는지 확인하여, 없으면 디렉토리부터만든다.
    if not os.path.exists(directory) :
        os.makedirs(directory)
    # 2. 디렉토리가 있으니, 파일을 저장.
    with open(os.path.join(directory, file.name), 'wb') as f :
        f.write(file.getbuffer())
    return st.success("Saved file : {} in {}".format(file.name, directory))

def main() :
    st.title('여러 파일들을 업로드')

    # 사이드바용 메뉴
    menu = ['Image','Csv','About']
    choice = st.sidebar.selectbox('메뉴',menu)
    if choice == 'Image' :
        uploaded_files = st.file_uploader('이미지파일 업로드',type=['png','jpeg','jpg']
                            ,accept_multiple_files=True)
        print(uploaded_files)
        
        if uploaded_files is not None:

            for file in uploaded_files:
                save_uploaded_file('temp_files',file)

                img = Image.open(file)
                st.image(img)

    elif choice == 'Csv':
        uploaded_csv = st.file_uploader('Csv파일 업로드', type='csv',accept_multiple_files=True)
        if uploaded_csv is not None:

            for csv in uploaded_csv:
                current_time = datetime.now()
                current_time = current_time.isoformat().replace(':', '_')
                csv.name = current_time + '.csv'
                save_uploaded_file('temp_Csvs',csv)
                df = pd.read_csv(csv)
                st.dataframe(df)
if __name__ == '__main__':
    main()