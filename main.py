import streamlit as st


name = st.text_input("Enter Your Name: ")
Fname = st.text_input("Enter your Father name: ")
adr = st.text_area("Enter Your Text: ")
classdata = st.selectbox("Enter Your Class :",(1,2,3,4,5,5))

button = st.button("Done")

if button :
    st.markdown(f"""
            Name : {name}
            Father Name : {Fname}
            address : {adr}
            class : {classdata}""")