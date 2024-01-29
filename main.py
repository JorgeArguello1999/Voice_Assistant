from configs.configs import obtener_url_desde_config
from api.request import make_request
from player.voice import reconocer_voz
from player.sound import reproducir_audio
from plyer import notification

# Función para interactuar con el chatbot a través de API
def api_chatbot(texto: str, url: str, name:str) -> None:
    if texto != False and name in texto:
        file_audio = make_request(message=texto, url= url)
        reproducir_audio(file_audio)

# Notificar lo que detecto
def notificacion(titulo:str, mensaje:str):
    notification.notify(
        title=titulo,
        message=mensaje,
        app_name='Bot',  
        timeout=10  
    )

if __name__ == "__main__":
    config_set = obtener_url_desde_config()
    while True:
        try:
            voz = reconocer_voz()
            notificacion(
                titulo='ChatBot',
                mensaje=voz
            )
            api_chatbot(
                texto= voz, 
                url= config_set["url"], 
                name= config_set["name"]
            )
        except Exception as e:
            break