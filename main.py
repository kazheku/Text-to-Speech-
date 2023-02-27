from operator import gt
from gtts import gTTS


language = "es" 
#Aquí puedes cambiar el idioma.

text = "Hola mundo, ¿Donde vives actualmente?"
#Introduce el texto que quieras convertir.

speech = gTTS(text=text, lang=language, slow=False)
