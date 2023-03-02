from gtts import gTTS
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

class TextToSpeechGUI:
    def __init__(self, master):
        self.master = master
        master.title("Text to Speech Converter")

        # Crear los widgets de la interfaz
        self.text_label = tk.Label(master, text="Introduzca el texto:")
        self.text_entry = tk.Entry(master, width=50)
        self.language_label = tk.Label(master, text="Idioma:")
        self.language_menu = tk.OptionMenu(master, tk.StringVar(), "es", "en", "fr", "de", "it")
        self.speed_label = tk.Label(master, text="Velocidad:")
        self.speed_menu = tk.OptionMenu(master, tk.BooleanVar(), False, True)
        self.save_button = tk.Button(master, text="Guardar como...", command=self.save_audio)
        self.exit_button = tk.Button(master, text="Salir", command=self.close_window)

        # Colocar los widgets en la interfaz
        self.text_label.grid(row=0, column=0, sticky="w")
        self.text_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        self.language_label.grid(row=2, column=0, sticky="w")
        self.language_menu.grid(row=3, column=0, padx=5, pady=5)
        self.speed_label.grid(row=2, column=1, sticky="w")
        self.speed_menu.grid(row=3, column=1, padx=5, pady=5)
        self.save_button.grid(row=4, column=0, pady=10)
        self.exit_button.grid(row=4, column=1, pady=10)


    def save_audio(self):
        # Obtener el objeto de conversión de texto a voz
        text = self.text_entry.get()
        language = self.language_menu.cget("text")
        speed = self.speed_menu.cget("text")
        speech = gTTS(text=text, lang=language, slow=speed)

        # Obtener el nombre de archivo y la ubicación para guardar el archivo de audio
        file_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=(("Archivos MP3", "*.mp3"),))

        # Guardar el archivo de audio
        try:
            speech.save(file_path)
            messagebox.showinfo("Guardar archivo", "Archivo guardado exitosamente!")
        except Exception as e:
            messagebox.showerror("Guardar archivo", f"No se pudo guardar el archivo: {e}")

    def close_window(self):
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    gui = TextToSpeechGUI(root)
    root.mainloop()
