import json

# Leemos el Archivo config.txt
def obtener_url_desde_config():
    try:
        with open("./configs/config.json", "r") as archivo_config:
            config_data = json.load(archivo_config)
            if 'url' in config_data:
                return {
                    "url": config_data['url'], 
                    "name": config_data['name']
                }

            else:
                print("No se encontró la URL en el archivo de configuración.")
                return None
    except FileNotFoundError:
        print("El archivo de configuración no existe")
        return None
    
    except Exception as e:
        print("Error: ", e)
        return None

if __name__ == '__main__':
    response = obtener_url_desde_config()
    print(response)