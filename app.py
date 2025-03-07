import streamlit as st

st.title('GitHub action and workflow test')

num = st.number_input('Enter a number', min_value=0, max_value=100, step=1)

if st.button('Square'):
    st.write(f'The square of {num} is {num*num}')