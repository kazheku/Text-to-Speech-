<h1> ¡Text-To-Speech! </h1>

## 📃 Explanation 

🔸 This is a 🔵**Python script**🔵 that creates a graphical user interface (GUI) for converting text to speech using the gTTS library. The GUI has several widgets, including a text entry box, a language selection dropdown menu, a speed selection dropdown menu, a "Save As" button for saving the generated audio file, and an "Exit" button for closing the GUI.

🔸 The user enters the text they want to convert into the text entry box, selects the desired language and speed from the dropdown menus, and clicks the "Save As" button to save the audio file in the desired location and format. If there is an error during the file saving process, the GUI displays an error message.

🔸 The gTTS library is used to generate the audio file. It takes the input text, selected language, and selected speed as parameters and returns an audio file in MP3 format. The file is then saved using the filedialog.asksaveasfilename method from the tkinter library.

🔸 Overall, this script provides an easy-to-use interface for generating audio files from text. The user can select their preferred language and speed, and save the audio file in the desired location and format.

⚠ This code is in beta version.
