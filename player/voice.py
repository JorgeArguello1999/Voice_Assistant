import speech_recognition as sr

# Función para grabar audio desde el micrófono y realizar reconocimiento de voz
def reconocer_voz():

    # Open a microphone
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Di algo...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Reconociendo...")
        # Usar reconocimiento de voz de Google
        texto = recognizer.recognize_google(audio, language='es-ES')
        return texto

    except sr.UnknownValueError:
        print("No se pudo entender lo que dijiste")
        return False

    except sr.RequestError as e:
        print(f"Error en la solicitud: {e}")
        return False

if __name__ == '__main__':
    response = reconocer_voz()
    print(response)