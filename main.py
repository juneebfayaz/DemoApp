import streamlit as st
import os
st.image(r"C:\Users\DELL\Desktop\img.jpeg",width=1024)
st.divider()
st.title("pahad")
name=st.text_input("enter your name")
age=st.number_input("enter your waens",min_value=18,max_value=100,step=5)
gender=st.selectbox("select your gender",["male","female","balai"])
subject=st.multiselect("select",["python","sql","css","java"])
login=st.button("Login")
st.image(os.path.join(os.getcwd(),"static","img.jpeg"))
if login:
    st.success("form submitted successfully")
    st.write(f"{name} your age is {age}")                         
    st.write("these are your subjects")
    
    for i in subject:
        st.write(f"{i}")
    st.write(f"gender : {gender}")


