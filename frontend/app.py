import os

import streamlit as st
from streamlit_option_menu import option_menu

from services.service import get_internship_data

import pandas as pd

import joblib


# Para iniciar el frontend, ejecuta el siguiente comando en la terminal desde la carpeta frontend:
# python -m streamlit run app.py

st.set_page_config(
    page_title='Interships Prediction',
    page_icon='🧑‍🎓',
    layout='wide'
)

@st.cache_resource
def cargar_modelo(nombre_modelo):
    modelos_archivos = {
        'Regresión Logística': 'logistic_regression.pkl',
        'Random Forest': 'random_forest_model.pkl',
        'XGBoost' : 'xgb_model.pkl',
        'LightGBM': 'lgb_model.pkl',
    }
    archivo = modelos_archivos.get(nombre_modelo)
    if archivo:
        ruta_completa = os.path.join('..', 'models', archivo)
        return joblib.load(ruta_completa)
    return None

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
                options= ['Regresión Logística', 'XGBoost', 'LightGBM', 'Random forest'],
                index = 0
            )
            cgpa = st.number_input(label='CGPA', min_value=5, max_value=10)
            skills_score = st.number_input(label='Puntuación de Skills', min_value=1, max_value=10, step=1)
            projects_count = st.number_input(label='Nº Proyectos', min_value=0, max_value=10, step=1)
        with col2:
            interships_done = st.number_input(label='Nº Prácticas Realizadas', min_value=0, max_value=5, step=1)
            communication_score = st.number_input(label='Puntuación Comunicación', min_value=5, max_value=10)
            coding_test_score = st.number_input(label='Puntuación del test de programación', min_value=0, max_value=10, step=1)
            resume_score = st.number_input(label='Puntuación del CV', min_value=0, max_value=5, step=1)
        with col3:
            certifications_count = st.number_input(label='Nº Certificados', min_value=1, max_value=10, step=1)
            github_score = st.number_input(label='Puntuación Github', min_value=0, max_value=5, step=1)
            extracurricular = st.checkbox(label='Extracurricular')
            soft_skills_score = st.number_input(label='Puntuación Soft Skills', min_value=5, max_value=10)

        with col4:
            interview_score = st.number_input(label='Puntuación de la entrevista', min_value=1, max_value=10, step=1)
            consistency_score = st.number_input(label='Puntuación de coherencia', min_value=0, max_value=10, step=1)
            backlogs = st.number_input(label='Backlogs', min_value=0, max_value=5, step=1)
            placement_training = st.checkbox(label='Participación en Programas de Formación')

        if modelo_selected:
            disabled = False

        btn_predict = st.form_submit_button('Predecir', type='primary', disabled=disabled)
        if btn_predict:
            with st.spinner('Realizando la predicción...'):
                try:
                    # Cargar el modelo elegido
                    pipeline = cargar_modelo(modelo_selected)
                    
                    # Construir el diccionario con las claves EXACTAS que espera el ColumnTransformer
                    datos_estudiante = {
                        'interview_score': [interview_score],
                        'skills_score': [skills_score],
                        'communication_score': [communication_score],
                        'coding_test_score': [coding_test_score],
                        'projects_count': [projects_count],
                        'soft_skills_score': [soft_skills_score],
                        'certifications_count': [certifications_count],
                        'resume_score': [resume_score],
                        'internships_done': [interships_done],
                        'extracurricular': [extracurricular],
                        'consistency_score': [consistency_score],
                        'placement_training': [placement_training],
                        'cgpa': [cgpa],
                        'github_score': [github_score],
                    }
                    
                    # Convertir a DataFrame (una sola fila)
                    X_nuevo = pd.DataFrame(datos_estudiante)
                    
                    # Clase predicha (0 o 1)
                    prediccion = pipeline.predict(X_nuevo)[0]

                    # Probabilidades
                    probas = pipeline.predict_proba(X_nuevo)[0]

                    prob_no_seleccionado = probas[0]
                    prob_seleccionado = probas[1]
                    
                    # Control por si la Regresión Lineal da valores negativos
                    if prediccion < 0:
                        prediccion = 0
                    
                    # Mostrar resultado de impacto en la UI
                    st.write('### ¡Resultados del simulador!')
                    
                    resultado_final = int(prediccion)
                    
                    if resultado_final == 1:
                        st.success("¡Enhorabuena!")
                        st.metric(
                            label=f"Predicción con {modelo_selected}",
                            value="✅ Ha sido seleccionado"
                        )
                    else:
                        st.error("Lo sentimos...")
                        st.metric(
                            label=f"Predicción con {modelo_selected}",
                            value="❌ No ha sido seleccionado"
                        )
                    st.write("### Probabilidades")
                    st.metric(
                        "Probabilidad de NO ser seleccionado",
                        f"{prob_no_seleccionado*100:.2f}%"
                    )

                    st.metric(
                        "Probabilidad de ser seleccionado",
                        f"{prob_seleccionado*100:.2f}%"
                    )
                except Exception as e:
                    st.error(f'Error al realizar la predicción. Asegurate que estén todas características seleccionadas: {e}')


elif selected == 'Prácticas':
    st.title('Prácticas')
    internships_data = load_data(get_internship_data())
    st.dataframe(internships_data)
else:
    st.text('Página no encontrada')