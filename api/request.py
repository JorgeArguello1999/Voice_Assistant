from dotenv import load_dotenv

import requests
import os 

# Cargando las variables de entorno
load_dotenv()
token = os.getenv('TOKEN')

def make_request(message:str, url:str) -> bin:
    try:
        response = requests.post(url, json={
            "ask": message, 
            "device": "bot",
            "token": token, 
            "user": "voice assistant"
        })

        if response.status_code != 200: return "Error"

        # Guardar el archivo de audio temporalmente
        with open('_temp_audio.mp3', 'wb') as archivo_audio:
            archivo_audio.write(response.content)
            return '_temp_audio.mp3'
        
    except requests.RequestException as e:
        print(f"Error en la solicitud al chatbot: {e}")

if __name__ == '__main__':
    url = 'https://chatbot-ojievlbbua-uc.a.run.app/api/'
    make_request(url=url, message='Hola como estas?')
