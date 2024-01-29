# Voice Assitant
Este proyecto tiene finalidad, utilizar la API de `Flupi` para realizar preguntas

## Configuración
En la carpeta `configs` vamos a tener un archivo que trae por nombre `config.json`.
``` json
// config.json
{
    "name": "Maxi", // Nombre del Bot
    "url": "url_de_la_api" 
}
```

## Variables de entorno 
Crearemos un archivo `.env` donde vamos a colocar la siguiente estructura
``` bash
TOKEN='your_token'
```

## Modulo para hablar con la API
Este modulo es el encargado de realizar la petición, puede variar dependiendo tu API, `api/request.py`
``` python 
def make_request(message:str, url:str) -> bin:
    try:
        # Aqui este JSON es la petición
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
``` 