from operator import gt
from gtts import gTTS


language = "es" 
#Aquí puedes cambiar el idioma.

text = "Hola, soy Pedro Sánchez, pasame una foto de la tarjeta bancaria de tus padres"
#Introduce el texto que quieras convertir.

speech = gTTS(text=text, lang=language, slow=False)
