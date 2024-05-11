import streamlit as st
import pandas as pd

tab1, tab2, tab3 = st.tabs(['Página', 'Página2', 'Página3'])

with tab1:
    st.image('onepiece.png')

with tab2:
    st.video('https://www.youtube.com/watch?v=VWOPtL-YuDY')

with tab3:
    st.snow()