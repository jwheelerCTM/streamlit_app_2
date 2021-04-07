import streamlit as st
import numpy as np
import pandas as pd
import time

st.title('My First App')
st.write('Joe Wheeler is the SEO and Python king.')
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    }))

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns = ['a', 'b', 'c'])

st.line_chart(chart_data)


if st.checkbox('Show dataframe'):
    chart_data_2 = pd.DataFrame(
        np.random.randn(20, 3),
        columns = ['a', 'b', 'c'])
    
    chart_data_2
    
    
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

df
    

option = st.selectbox(
    'Is SEO cool?',
    df['first column'])

'You selected: ', option


option_2 = st.sidebar.selectbox(
    'Which other number do you like?',
    df['second column'])

'You selected: ', option_2

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'
