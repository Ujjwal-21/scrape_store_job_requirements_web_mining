from scrape import scrape_main
from dbms import mdb

# q=input("Enter your job title: ")
# print(scrape_main.getSkills(q,1))
# q=input("Enter your job title: ")
# print(scrape_main.getSkills(q,1))

import streamlit as st
import pandas as pd
import numpy as np
page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
    background-image: url('https://media.istockphoto.com/id/514411672/photo/office-leather-desk-table-with-coffee-and-supplies.jpg?b=1&s=170667a&w=0&k=20&c=0KteWdUsdVG0_UUNQXoJ6q6CemQAOg5ux0XN_vSsDgc=');
    background-size: cover;
}
[data-testid="stSidebar"] {
    background-color: rgba(0,0,0,0.0);
}
h1{
    color: #FFFFFF;
}
table{
    background-color: #00425A;
    text-align: center;
}

</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("JOB SKILLS RECOMMENDATION SYSTEM")

option1 = st.text_input('Select Job Title')
intensity = st.slider('Search Intensity', 1, 10, 5)
show = st.slider('Show these many skills (set 0 for all)', 0, 50, 10)
if st.button('Search'):
    st.write("Skills required for ",option1," are:")
    o=mdb.queryList(option1)
    if o!=[]:
        st.table(pd.DataFrame(o if show==0 else o[0:show]))
    else :
        o=scrape_main.getSkills(option1,intensity)
        st.table(pd.DataFrame(o if show==0 else o[0:show]))