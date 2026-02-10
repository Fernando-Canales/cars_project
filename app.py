"""
Docstring for app

Created by Fernando on Feb. 10 2026
"""
import pandas as pd
import plotly.express as px
import streamlit as st

# leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# crear casillas de verificación
build_histogram = st.checkbox('Construir histograma')
build_scatter = st.checkbox('Construir gráfico de dispersión')

# histograma
if build_histogram:
    st.write(
        'Creación de un histograma para el conjunto de datos '
        'de anuncios de venta de coches'
    )

    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

# gráfico de dispersión
if build_scatter:
    st.write(
        'Creación de un gráfico de dispersión entre el odómetro '
        'y el precio de los coches'
    )

    fig = px.scatter(
        car_data,
        x='odometer',
        y='price'
    )

    st.plotly_chart(fig, use_container_width=True)