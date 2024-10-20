from google_speech import Speech

# say "Hello World"
text = " Explora el tablero de Loana Tarifa cuentos cortos para niños en Pinterest. Ver más ideas sobre cuentos cortitos, cuentos cortos para imprimir, cuentos infantiles para leer."
lang = "es"
speech = Speech(text, lang)

# you can also apply audio effects while playing (using SoX)
# see http://sox.sourceforge.net/sox.html#EFFECTS for full effect documentation
# sox_effects = ("speed", "1.5")
# speech.play(sox_effects)

# save the speech to an MP3 file (no effect is applied)
speech.save("output.mp3")
