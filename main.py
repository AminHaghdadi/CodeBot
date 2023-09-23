import streamlit as st
from model import qa_bot

st.title("Code Helper 🖥️")
st.sidebar.subheader(("This ChatBot is powerd by Microsoft StableCode."),divider='rainbow')
st.sidebar.subheader("Data is available in the link below:")
st.sidebar.write("https://github.com/sahil280114/codealpaca")
st.sidebar.write("https://github.com/teknium1/GPTeacher")



query= st.text_area('Enter your question here:')
button=st.button('Submit')

if button :
    response=qa_bot(query)
    result=response['result']
    source=response['source_documents'][0]
    st.code(result)
    st.caption('source:')
    st.write(source)



