import streamlit as st
st.title("選擇元素")

option_select = st.selectbox("你喜歡的顏色是什麼?",["紅","綠","藍"])
st.write(f"你選擇的顏色是:{option_select}")

option_mul =  st.multiselect("你喜歡的水果是",["蘋果","香蕉","橘子"])
st.write(f"你選擇的水果是:{option_mul}")

dataList = ["春","夏","秋","冬"]
option_radio = st.radio("你喜歡的季節是?",dataList)
st.write(f"你選擇的季節是:{option_radio}")

checkbox = st.checkbox("是否同意?")
if checkbox:
    st.write("同意")
else:
    st.write("不同意")
st.write(checkbox)





