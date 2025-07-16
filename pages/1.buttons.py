import streamlit as st

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