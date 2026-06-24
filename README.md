# 🧑‍🎓 Football Market Value Predictor: ML Regression & MLOps

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-v0.100+-009688.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-v1.25+-FF4B4B.svg)
![SQLite](https://img.shields.io/badge/SQLite-v3.0+-003B57.svg)
![XGBoost](https://img.shields.io/badge/XGBoost-v1.7+-111111.svg)

Este repositorio contiene una solución integral end-to-end desarrollada para abordar un problema de **Clasificación**: la predicción de **un alumno en ser contratado con su perfil académico**. La arquitectura implementada destaca por su enfoque desacoplado, integrando almacenamiento relacional local, una capa de servicio mediante API, experimentación con múltiples modelos y un frontend interactivo.

---

## 📌 1. Origen de Datos y Alcance

En lugar de utilizar la sugerencia por defecto del briefing, apostamos por la autenticidad utilizando un ecosistema de datos estudiantiles extraído de **Kaggle**. Consolidamos la información a partir de tres conjuntos de datos relacionales:
*`Internship_Selection_Dataset.csv`: Datos estudiantiles de los usuarios.


---

## 🛠️ 2. Arquitectura del Sistema

El proyecto está diseñado bajo principios de modularidad, dividiendo las responsabilidades en capas independientes[cite: 1]:

1.  **Almacenamiento (Persistencia):** Tras un proceso exhaustivo de limpieza y preprocesamiento, los datos estructurados se almacenan de forma local en una base de datos relacional **SQLite**.
2.  **Capa de Servicio (Backend):** Implementada con **FastAPI**. Funciona como el motor de la aplicación, conectándose a SQLite y exponiendo endpoints seguros para consultar la información. Esta estructura sienta las bases para un pipeline de ingesta automatizado.
3.  **Capa de Presentación (Frontend):** Una aplicación multipágina desarrollada en **Streamlit**. Consume la API de FastAPI para ofrecer:
    *   **Visualización de los datos** Visualizaciones de los datos almacenados en la bbdd.
    *   **Demo Interactiva** (Simulador en tiempo real donde el usuario introduce datos del estudiante y el modelo predice si será contratado o no).

---

## 🤖 3. Modelado de Machine Learning

Se evaluaron y compararon cuatro algoritmos de regresión para encontrar el equilibrio óptimo entre precisión y generalización:

*   **Logistic Regression:** Nuestro modelo base para analizar relaciones lineales y predecir la probabilidad de un evento categórico (como éxito/fracaso).
*   **Random Forest:** CUn modelo de ensamble (Bagging) compuesto por múltiples árboles de decisión independientes que captura relaciones complejas y patrones no lineales mediante votación mayoritaria.
*   **LightGBM:** Un framework avanzado de Gradient Boosting basado en árboles de decisión, diseñado para ser altamente eficiente y rápido con grandes volúmenes de datos.
*   **XGBoost Classificator (Ensemble):** Un modelo avanzado de Gradient Boosting que entrena árboles de decisión de forma secuencial, minimizando los errores de los árboles anteriores mediante regularización para optimizar la métrica objetivo.

**Variables Predictoras (Features):** Nota final de los estudios, puntuación de differentes áreas como Linkedin, GitHub, Soft Skills...

---

## 📂 4. Estructura del Repositorio

```text
├── backend/
│   ├── internship_data.db
│   └── main.py
├── data/
│   ├── clean/
│   │   ├── importancia_variables.csv
│   │   ├── Intsernship_Selection_Dataset.csv
│   └── raw/
├── frontend/
│   ├── services/
│   │   ├── __init__.py
│   │   └── services.py
│   └── app.py
├── models/
│   ├── lgb_model.pkl
│   ├── logistic_regression.pkl
│   ├── random_forest.pkl
│   └── xgb_model.pkl
├── notebooks/
│   ├── arbol_decisiones.ipynb
│   ├── clubs-cleaning.ipynb
│   ├── competitions-cleaning.ipynb
│   ├── informe_EDA.ipynb
│   ├── logistic_regression.ipynb
│   ├── players-cleaning.ipynb
│   ├── train_model_KNN.ipynb
│   └── xgboost.ipynb
├── .env
├── .env-example
├── .gitignore
├── README.md
└── requirements.txt
````

---

## 🚀 5. Instrucciones de Ejecución Local

1. **Clonar el repositorio e instalar dependencias**
```bash
git clone [https://github.com/Bootcamp-DA-P2/DA-project-classification-Grupo2](https://github.com/Bootcamp-DA-P2/DA-project-classification-Grupo2)
cd DA-Project-classification-Grupo2
pip install -r requirements.txt

2. Desplegar el Backend (FastAPI)
Inicia el servidor local que conecta la base de datos con los modelos de ML:

cd backend
uvicorn main:app --reload --port 8000
(Puedes interactuar con los endpoints directamente en http://localhost:8000/docs)

3. Lanzar el Frontend (Streamlit)
En una pestaña o ventana de terminal nueva y paralela, ejecuta la aplicación visual:

Bash
cd frontend
streamlit run app.py / python -m streamlit run app.py
(La aplicación se abrirá automáticamente en tu navegador web local en el puerto 8501)

## 👥 6. Metodología de Trabajo y Gestión del Proyecto

Para garantizar el cumplimiento de los objetivos en el plazo estipulado de 1 semana, el equipo adoptó un enfoque metodológico ágil, fundamentado en la comunicación continua y el seguimiento estructurado de tareas.

### 📋 Gestión de Tareas con GitHub Projects
La organización interna del grupo se centralizó utilizando **GitHub Projects**, configurando un tablero automatizado basado en el marco de trabajo **Kanban**. Esto nos permitió mantener la trazabilidad de los entregables y asegurar que cada componente crítico fuera cubierto a tiempo.



## 👥 Integrantes del Equipo

* **Marco Ohimai Imouokhome Pilares**
* **Miguel Ángel Moreno**
* **Daniel Luque Gallardo**
