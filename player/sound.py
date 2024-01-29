import pygame

# Función para reproducir archivo de audio
def reproducir_audio(ruta_archivo):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(ruta_archivo)
    pygame.mixer.music.play()

    # Mantener el programa en ejecución hasta que termine la reproducción
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10) 

    pygame.mixer.music.stop()
    pygame.quit()

