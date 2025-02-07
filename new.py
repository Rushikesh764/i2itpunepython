import pandas as pd
import numpy as np
import streamlit as st

st.title("rushikesh")
st.write("python required practice")

data = pd.DataFrame({
    'c1': [10, 20, 30, 40],
    'c2': ['A', 'B', 'C', 'D']
})
st.write("below is the table for the data")
st.write(data)

char_data = pd.DataFrame(np.random.rand(20, 3), columns=['A', 'B', 'C'])
st.line_chart(char_data)
st.bar_chart(char_data)
st.area_chart(char_data)

