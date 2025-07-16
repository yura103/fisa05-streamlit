import streamlit as st
import pandas as pd

ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

# 입력을 변수로 받아서 해당 텍스트와 같은지를 판단하는 작업 수행
search_text = st.text_input('Search for an anime:')
if search_text:
    if search_text in ani_list:
        st.image(img_list[ani_list.index(search_text)])
    else:
        st.write('No matching anime found.')