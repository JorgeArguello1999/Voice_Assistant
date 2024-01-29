import requests 
import os

from configs.configs import obtener_url_desde_config
from player.voice import reconocer_voz
from player.sound import reproducir_audio

# Función para interactuar con el chatbot a través de API
def api_chatbot(texto: str, url: str, name:str) -> None:
    if texto != False and name in texto:
        try:
            response = requests.post(url, json={"ask": texto, "device": "bot"})

            if response.status_code != 200:
                print("Error al obtener el archivo de audio")
                return

            # Obtener el contenido del archivo de audio
            audio_content = response.content

            # Guardar el archivo de audio temporalmente
            nombre_archivo = '_temp_audio.mp3'
            with open(nombre_archivo, 'wb') as archivo_audio:
                archivo_audio.write(audio_content)
                print(f"Archivo de audio guardado como {nombre_archivo}")

            reproducir_audio(nombre_archivo)

        except requests.RequestException as e:
            print(f"Error en la solicitud al chatbot: {e}")

        finally:
            if os.path.exists(nombre_archivo):
                # Eliminar archivo de audio temporal si existe
                os.remove(nombre_archivo)  

if __name__ == "__main__":
    config_set = obtener_url_desde_config()
    while True:
        try:
            api_chatbot(
                texto= reconocer_voz(), 
                url= config_set["url"], 
                name= config_set["name"]
            )
        except Exception as e:
            break