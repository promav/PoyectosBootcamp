import streamlit as st
import joblib
import seaborn as sns
import pandas as pd 

if st.button('Volver a inicio'): # opcional poder volver a inicio
    st.switch_page('app.py')

@st.cache_resource
def load_scikit_model():
    return joblib.load('models/pipeline_regresion.joblib')

@st.cache_resource
def load_dataset():
    url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/diamonds.csv'
    return pd.read_csv(url)

st.title('Página 2 - Regresión')

model = load_scikit_model()

st.write('Ejemplo de los datos')
df = load_dataset()
price_mean = df['price'].mean() # precio medio de todo el dataset

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
    cut = st.selectbox('Introduce tipo de cut', df['cut'].unique().tolist())
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
            'cut': [cut],
            'color': [color],
            'clarity': [clarity],
            'depth': [depth],
            'table': [table],
            'x':[x],
            'y':[y],
            'z':[z],                 
        })
        prediccion = model.predict(X_new)[0] # esta prediccion se podría guardar en base de datos junto a los datos introducidos
        # st.write(prediccion)
        delta_value = prediccion - price_mean
        col1, col2 = st.columns(2)
        col1.metric('Precio estimado (predicción)', value=f'{prediccion:.2f} $', delta=f'{delta_value:.2f} $')
        col2.metric('Precio medio', value=f'{price_mean:.2f} $')

    
    
    