import streamlit as st
import joblib
import seaborn as sns
import pandas as pd
from sklearn.preprocessing import LabelEncoder

if st.button('Volver a inicio'): # opcional poder volver a inicio
    st.switch_page('app.py')

@st.cache_resource
def load_scikit_model():
    return joblib.load('models/pipeline_clasificador.joblib')

@st.cache_resource
def load_dataset():
    url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/diamonds.csv'
    return pd.read_csv(url)

st.title('Página 3 - Clasificación')

model = load_scikit_model()

st.write('Ejemplo de los datos')
df = load_dataset()

st.table(df.head())

# 2. Formulario para predicción
st.header('Introduce datos para la predicción')

with st.form("Diamonds_form"):
    carat = st.number_input(
                    'Introduce total carat', 
                    min_value=0.0, max_value=10.0, 
                    value=df['carat'].mean(), 
                    step=0.01
    )
    color = st.selectbox('Introduce el color', df['color'].unique().tolist())
    clarity = st.selectbox('Introduce el tipo de clarity', df['clarity'].unique().tolist())
    
    depth = st.number_input(
                    'Introduce total depth', 
                    min_value=df['depth'].min(), max_value=df['depth'].max(), 
                    value=df['depth'].mean(), 
                    step=0.01
    )
    
    table = st.number_input(
                    'Introduce total table', 
                    min_value=df['table'].min(), max_value=df['table'].max(), 
                    value=df['table'].mean(), 
                    step=0.01
    )
    
    price = st.number_input(
                    'Introduce total price', 
                    min_value=0, max_value=20000, 
                    value=int(df['price'].mode().iloc[0]), 
                    step=1
    )
    
    x = st.number_input(
                    'Introduce total x', 
                    min_value=df['x'].min(), max_value=df['x'].max(), 
                    value=df['x'].mean(), 
                    step=0.01
    )
    
    y = st.number_input(
                    'Introduce total y', 
                    min_value=df['y'].min(), max_value=df['y'].max(), 
                    value=df['y'].mean(), 
                    step=0.01
    )
    
    z = st.number_input(
                    'Introduce total z', 
                    min_value=df['z'].min(), max_value=df['z'].max(), 
                    value=df['z'].mean(), 
                    step=0.01
    )

    boton_enviar = st.form_submit_button("Generar predicción")

    if boton_enviar:
        X_new = pd.DataFrame({
            'carat': [carat],
            'color': [color],
            'clarity': [clarity],
            'depth': [depth],
            'table': [table],
            'price': [price],
            'x':[x],
            'y':[y],
            'z':[z],                 
        })
        prediccion = model.predict(X_new) # esta prediccion se podría guardar en base de datos junto a los datos introducidos
        # st.write(prediccion)
        proba = model.predict_proba(X_new).max() * 100
        col1, col2 = st.columns(2)
        col1.metric('Tipo de corte estimado', value=prediccion[0])
        col2.metric('Probabilidad', value=f'{proba:.2f} %')

    
    
    