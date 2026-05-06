import streamlit as st



colorDir = {"紅色":0,"藍色":1,"綠色":2}

st.title("選擇顏色")
data = ["紅色","藍色","綠色"]
option_index = st.selectbox("你喜歡的顏色是?",data)
st.write(f"你選的顏色:{colorDir[option_index]}")

dataList = list(range(1,11))
option_radio = st.select_slider("選一個範圍",options=dataList,value=(3,6))
st.write(f"你選的範圍:{option_radio}")

value = st.slider("選範圍",0.0,100.0,value=(25.2567,75.212))
st.write(f"你選的範圍:{value}")