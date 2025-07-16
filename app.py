import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)

# st.bar_chart(df.rating, x_label=df.command, y_label='Rating')
# streamlit의 defualt chart는 altair라는 다른 라이브러리

# Plotly Bar Chart
fig = px.bar(
    df,
    x="command",     # x축에 command
    y="rating",      # y축에 rating
    color="command", # command별 색깔 구분
    labels={"command": "x축 제목", "rating": "Rating"},
    title="Command Rating Bar Chart"
)
# # Streamlit에 출력: use_container_width=True to fit the chart to the container width
st.plotly_chart(fig) #, #use_container_width=True)


# 입력
st.button('Demo')
st.data_editor(df)
st.checkbox('Option 1')
country = st.radio('Pick Country:', ['France','Germany'])
st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])
st.slider('Slide me', min_value=0, max_value=10)
st.select_slider('Slide to select', options=[1,'2'])
st.text_input('Enter Article')
st.number_input('Enter required number')
st.text_area('Entered article text')
st.date_input('Select date')
st.time_input('Select Time')
st.file_uploader('File CSV uploader')
data = '''This is a sample text file for download'''
st.download_button('Download Source data', data)
st.camera_input('Click a Snap')
st.color_picker('Pick a color')

# 출력
st.text('Tushar-Aggarwal.com')
st.markdown('[Tushar-Aggarwal.com](https://tushar-aggarwal.com)')
st.caption('Success')
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.write('Supreme Applcations by Tushar Aggarwal')
st.write(['st', 'is <', 3]) # see *
st.title('Streamlit Magic Cheat Sheets')
st.header('Developed by Tushar Aggarwal')
st.subheader('visit tushar-aggarwal.com')
st.code('for i in range(8): print(i)')
st.image('https://i.imgur.com/t2ewhfH.png')
# * optional kwarg unsafe_allow_html = True


ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

st.code(ani_list)
st.write(ani_list)

for ani in ani_list:
    st.write(ani)

# 입력을 변수로 받아서
# 1. 버튼을 누르면 화면에 True라고 코드를 리턴하는 간단한 함수 작성
# 2. 사진을 찍으면 다운로드 버튼으로 사진을 다운로드 받을 수 있게 작성
a = st.button('클릭')
st.write(a)

if st.button('클릭2'):
    st.write('True')
print(a) # 화면이 아니라 콘솔

if image := st.camera_input('Click a Snap2'):
    st.download_button('다운로드', image, 'my.png')