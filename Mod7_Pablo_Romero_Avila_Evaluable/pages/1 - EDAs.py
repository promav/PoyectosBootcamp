
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.title('Página 1 - EDAs')

if st.button('Volver a inicio'): # opcional poder volver a inicio
    st.switch_page('app.py')
    
@st.cache_resource
def load_dataset():
    url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/diamonds.csv'
    return pd.read_csv(url)

st.header('1. Filtros Globales')
st.subheader('Filtros categóricos')
df = load_dataset()

# Filtro cut 
cut = df['cut'].unique().tolist()
selected_cut = st.multiselect('Selecciona los tipos de corte.', options=cut, default=cut)

# Filtro color 
color = df['color'].unique().tolist()
selected_color = st.multiselect('Selecciona los tipos de color.', options=color, default=color)

# Filtro clarity 
clarity = df['clarity'].unique().tolist()
selected_clarity = st.multiselect('Selecciona los tipos de claridad.', options=clarity, default=clarity)


st.subheader('Filtros numéricos')

carat_min, carat_max = st.slider(
    'Selecciona rango de carat', 
    min_value=df['carat'].min(),
    max_value=df['carat'].max(),
    value=(df['carat'].min(), df['carat'].max())
)

depth_min, depth_max = st.slider(
    'Selecciona rango de depth', 
    min_value=df['depth'].min(),
    max_value=df['depth'].max(),
    value=(df['depth'].min(), df['depth'].max())
)

table_min, table_max = st.slider(
    'Selecciona rango de table', 
    min_value=df['table'].min(),
    max_value=df['table'].max(),
    value=(df['table'].min(), df['table'].max())
)

price_min, price_max = st.slider(
    'Selecciona rango de price', 
    min_value=df['price'].min(),
    max_value=df['price'].max(),
    value=(df['price'].min(), df['price'].max())
)

st.header('2. Carga de datos filtrados')

df_filtered = df[
    (df['cut'].isin(selected_cut)) &
    (df['color'].isin(selected_color)) &
    (df['clarity'].isin(selected_clarity)) &
    (df['carat'] >= carat_min) & (df['carat'] <= carat_max) &
    (df['depth'] >= depth_min) & (df['depth'] <= depth_max) &
    (df['table'] >= table_min) & (df['table'] <= table_max) &
    (df['price'] >= price_min) & (df['price'] <= price_max)
]

st.dataframe(df_filtered, use_container_width=True)

st.write(f'Nº filas antes de filtrar: **{df.shape[0]}**')
st.write(f'Nº filas después de filtrar: **{df_filtered.shape[0]}**')
st.write(f'Nº filas eliminadas por filtro: **{df.shape[0] - df_filtered.shape[0]}**')

st.header('3. Gráficos univariantes')

st.subheader('Histograma sobre precio')
fig, ax = plt.subplots(figsize=(6,4))
sns.histplot(df_filtered, x='price', kde=True)
ax.set_title('Analisis univariante price')
st.pyplot(fig)

st.subheader('Value count sobre cut')
fig, ax = plt.subplots(figsize=(6,4))
sns.countplot(df_filtered, x='cut')
ax.set_title('Analisis univariante cut')
st.pyplot(fig)

st.header('4. Gráficos bivariantes')

st.subheader('Scaterplot Carat-Price (Sample 2000)')
fig, ax = plt.subplots(figsize=(6,4))
sns.scatterplot(df_filtered.sample(2000), x='carat', y='price')
ax.set_title('Analisis bivariante, carat-price')
st.pyplot(fig)

st.subheader('Box-plot price - cut')
fig, ax = plt.subplots(figsize=(10,8))
sns.boxplot(df_filtered, y='price', hue='cut')
ax.set_title('Boxplot')
st.pyplot(fig)

st.header('5. Gráficos multivariantes')
st.subheader('Heatmap')
fig, ax = plt.subplots(figsize=(10,8))
sns.heatmap(df_filtered.corr(numeric_only=True), annot=True, cmap='viridis')
ax.set_title('Matriz de correlaciones')
st.pyplot(fig)