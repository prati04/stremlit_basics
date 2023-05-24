import streamlit as st
import pandas as pd
import numpy as np

st.title('Help Center')

def getanswer(query):
	answer = "answer for this query"
	return answer

query = st.text_input('Your query', '', key=id)


if query:
    answer = getanswer(query)
    st.success('The result of your query is '+ answer)
        

