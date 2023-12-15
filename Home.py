import streamlit as st

st.title('การทดสอบเขียนเว็บด้วย Python')
st.header("Chuthiwat khamsakhon")
st.subheader('สาขาวิชาเทคโนโลยีสารสนเทศ')
st.markdown("----")

col1, col2 = st.columns(2)
#col1.write("This is column 1")
#col2.write("This is column 2")
with col1:
    st.image('./pic/nice.jpg')
with col2:
    st.image('./pic/iris.jpg')