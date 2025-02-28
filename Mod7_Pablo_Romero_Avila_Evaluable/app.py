
import streamlit as st

st.title('MODULO 7 - STREAMLIT')
st.write('''
         Aplicacion de Streamlit para EDA, regresión y clasificación.
         
         Para la práctica del módulo 7 basada en el DataSet de Diamonds''')

col1, col2, col3 = st.columns(3)

with col1:
    if st.button('Ir a EDAs'):
        st.switch_page('pages/1 - EDAs.py')
        
with col2:
    if st.button('Ir a Regresión'):
        st.switch_page('pages/2 - Regresión.py')
        
with col3:
    if st.button('Ir a Clasificación'):
        st.switch_page('pages/3 - Clasificación.py')