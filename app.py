import streamlit as st 
import pandas as pd 

st.title('Solver Platform')

data = st.file_uploader('Insert File Data')
df = pd.read_csv(data)
st.dataframe(df) 
