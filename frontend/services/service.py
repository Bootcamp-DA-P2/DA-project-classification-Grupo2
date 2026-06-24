import requests
from dotenv import load_dotenv
import os

load_dotenv()
URL_BACKEND_INTERNSHIPS = os.getenv('URL_BACKEND_INTERNSHIPS')

def get_intership_data():
    try:
        response = requests.get(URL_BACKEND_INTERNSHIPS)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        raise Exception(f'Error en la conexión de la API: {e}')
