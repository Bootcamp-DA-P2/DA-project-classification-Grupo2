import streamlit as st
from streamlit_option_menu import option_menu
from services.service import get_intership_data

# Para iniciar el frontend, ejecuta el siguiente comando en la terminal desde la carpeta frontend:
# python -m streamlit run app.py

st.set_page_config(
    page_title='Interships Prediction',
    page_icon='🧑‍🎓',
    layout='wide'
)

@st.cache_data
def load_data(function):
    return function

selected = option_menu(None, ["Predicciones", "Prácticas"], icons= ['briefcase', 'book'], orientation='horizontal', default_index=0)

if selected == 'Predicciones':
    st.title('Predicciones de estudiantes realizando sus prácticas')
    st.subheader('Introduce las características del estudiante para determinar la probabilidad de que sea contratado.')

    with st.form('formulario_predicción'):
        disabled = True
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            modelo_selected = st.selectbox(
                'Modelo de Predicción',
                options= ['regresión Lineal', 'XGBoost', 'Random forest'],
                index = 0
            )
        with col2:
            pass
        with col3:
            pass
        with col4:
            pass

        if modelo_selected:
            disabled = False

        btn_predict = st.form_submit_button('Predecir', type='primary', disabled=disabled)
        if btn_predict:
            with st.spinner('Realizando la predicción...'):
                try:
                    st.text('Funciona')
                except Exception as e:
                    st.error(f'Error al realizar la predicción. Asegurate que estén todas características seleccionadas: {e}')


elif selected == 'Prácticas':
    st.title('Prácticas')
    interships_data = load_data(get_intership_data())
    st.dataframe(interships_data)
else:
    st.text('Página no encontrada')