from configs.configs import obtener_url_desde_config
from api.request import make_request
from player.voice import reconocer_voz
from player.sound import reproducir_audio

# Función para interactuar con el chatbot a través de API
def api_chatbot(texto: str, url: str, name:str) -> None:
    if texto != False and name in texto:
        file_audio = make_request(message=texto, url= url)
        reproducir_audio(file_audio)

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