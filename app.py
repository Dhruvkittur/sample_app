import streamlit as st
st.title("MY FIRST STEAMLIT APP")


name=st.text_input("Enter your Name")
if st.button("Submit"):
   st.write(f"Hello,{name}")


age=st.number_input("Enter your age")
if st.button("Check Eligibility"):
   if age>=18:
      st.success("Eligible to vote")
   else:
      st.write("Sorry not eligible") 
   

   
