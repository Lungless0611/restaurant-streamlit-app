import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Restaurant Insights')
st.write('¿El total de consumo de los clientes afecta a las propinas de los meseros?')

rest_data = pd.read_csv('restaurant_data.csv')
rest_data['bill_datetime'] = pd.to_datetime(rest_data['bill_datetime'])

min_bill = float(rest_data['restaurant_bill'].min())
max_bill = float(rest_data['restaurant_bill'].max())

# Slider (línea con bolita)
total_account = st.slider(
    "Mostrar solo cuentas >= a est valor:", min_bill, max_bill, min_bill)

# Filtro para el sliderr.
filtered_data = rest_data[rest_data['restaurant_bill'] >= total_account]

# Checkboxes
checkbox_histograma = st.checkbox('Mostrar histograma')
checkbox_scatter = st.checkbox('Mostrar dispersión (scatter)')

# Botón para accionar
start_button = st.button('Botón misterioso 🙀🙀🙀')

# lo que pasará cuando presione el boton

if checkbox_histograma:
    st.write('Histograma de total de la cuenta')
    fig_hist = px.histogram(filtered_data, x='restaurant_bill')
    st.plotly_chart(fig_hist, use_container_width=True)

if checkbox_scatter:
    st.write('consumo y propina')
    fig_scatter = px.scatter(
        filtered_data,
        x='restaurant_bill',
        y='tips',
        color='waiter_sex',
        title='Restaurant Bill vs Tips'
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

    # <-- No tenía idea de esto, chatgpt me recomendó agregar esto
    if not checkbox_histograma and not checkbox_scatter:
        st.warning("Selecciona al menos un gráfico antes de ejecutar.")
    # Obviamente no lo hice todo con chatgpt pero, me ayudó a pulir algunas cosas. También con la lógica de la interacción
    # Espero que funcione!!!!!!, estoy emocionado 🙀
if start_button:  # jejejej
    st.snow()
    st.header("HELLO WORLD")
    st.success("Has desbloqueado un logro!")
    st.markdown(
        "[Clic aquí para reclamar tu premio 😼🎁](https://www.youtube.com/shorts/SXHMnicI6Pg)")
if 53 < total_account < 54:  # Un easter_egg, ando experimentando
    st.image("secreto.jpg")
    st.balloons()
    st.write("Has encontrado un easter egg 🙀😹✨")
