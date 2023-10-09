

# Solicita la frase y el idioma de destino
frase = input("Ingresa la frase que quieres traducir: ")
idioma_destino = input("Ingresa el idioma de destino (por ejemplo, 'es' para español): ")
# Crea una instancia del traductor
traductor = Translator()
# Traduce la frase al idioma de destino
traduccion = traductor.translate(frase, dest=idioma_destino)
frase_traducida = traduccion.text
# Crea una instancia de gTTS para generar el audio
# Imprime la frase traducida
print("Frase traducida:", frase_traducida)
tts = gTTS(text=frase_traducida, lang=idioma_destino)
tts.save("temp.wav")
sound_file = "temp.wav"
Audio(sound_file, autoplay=True)

