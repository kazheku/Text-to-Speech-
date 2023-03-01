<h1> ¡Text-To-Speech! </h1>

## Explanation 

This 🔵 **Python code** 🔵 uses the **gTTS (Google Text-to-Speech) library** to generate an audio file from the given text.

First, it imports the **gt** (greater than) operator and the **gTTS** class from the **gtts** module.

It then sets the **language** variable to the desired language code (e.g. 'es' for Spanish).

Next, it sets the **text** variable to the input text that will be converted to speech.

Finally, it creates an instance of the **gTTS** class by passing the input text and language code as arguments, along with the **slow** parameter set to **False** to generate audio at normal speed. 
The resulting gTTS object can then be saved to an audio file using its **save()** method.

⭕ Note that the gTTS library requires an internet connection to generate the audio file, as it sends the text to the Google Text-to-Speech API to generate the audio.

⚠ This code is in beta version, I will keep working on it to create a more professional GUI and improve the code.
