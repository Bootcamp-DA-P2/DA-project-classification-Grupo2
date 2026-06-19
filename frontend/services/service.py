import requests
from dotenv import load_dotenv
import os

load_dotenv()
URL_BACKEND_INTERSHIPS = os.getenv('URL_BACKEND_INTERSHIPS')

def get_intership_data():
    try:
        response = requests.get(URL_BACKEND_INTERSHIPS)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        raise Exception(f'Error en la conexión de la API: {e}')
