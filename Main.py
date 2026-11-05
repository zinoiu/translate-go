import customtkinter as ctk
import speech_recognition as sr
from googletrans import Translator, LANGUAGES

#Translation
class translatorApp:
    def __init__(self):
        self.language_mapping ={lang_name.capitalize(): lang_code for lang_code, lang_name in LANGUAGES.items()}

    def speech_to_text(self):
        recognizer = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("You can speak now...")
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=15)
        except (OSError, sr.WaitTimeoutError) as e:
            print(f"Microphone unavailable: {e}")
            return None

        try:
            text = recognizer.recognize_google(audio)
            print(f"Original Text: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from the recognition service; {e}")
        return None

    def speech_to_tex(self):
        return self.speech_to_text()
    
    def translate_text(self, text, target_language):
        translator = Translator ()
        try:
            translated = translator.translate(text, dest=target_language)
            return translated.text
        except Exception as e:
            print(f"Translation failed: {e}")
            return "Translation error, please try again later."
        
# App
class TranslatorAppGUI(ctk.CTk):
    def __init__(self, translator_app):
        super().__init__()
        self.translator_app = translator_app

        self.title("Translate Go")
        self.geometry("700x500")

        self.create_widgets()
    
    def create_widgets(self):
        self.label_instruction = ctk.CTkLabel(self, text= "Choose input method and language for translation", font= ("Vogue Regular", 25))
        self.label_instruction.pack(pady=20)

        self.input_choice_var = ctk.StringVar(value="text")
        self.radio_voice = ctk.CTkRadioButton(self, text="Voice Input", variable=self.input_choice_var, value="voice", font=("Rockwell Regular", 18))
        self.radio_voice.pack(pady=10)

        self.radio_text = ctk.CTkRadioButton(self, text="Text Input", variable=self.input_choice_var, value="text", font=("Rockwell Regular", 18))
        self.radio_text.pack(pady=10)

        self.voice_button = ctk.CTkButton(self, text="Start Voice Input", command=self.handle_voice_input, font=("Rockwell Regular", 16))
        self.voice_button.pack(pady=10)

        self.text_box = ctk.CTkTextbox(self, width= 300, height= 80, font=("Rockwell Regular", 20))
        self.text_box.pack(pady=10)

        self.translate_button = ctk.CTkButton(self, text="Translate", font=("Rockwell Regular", 16), command=self.handle_translation)
        self.translate_button.pack(pady=10)

        self.translated_label = ctk.CTkLabel(self, text="", font=("Rockwell Regular", 20), wraplength=400)
        self.translated_label.pack(pady=10)

        self.language_frame = ctk.CTkFrame(self)
        self.language_frame.pack(pady=10)
        self.language_label = ctk.CTkLabel(
            self.language_frame,
            text="Choose target language:",
            font=("Rockwell Regular", 16),
        )
        self.language_label.pack(side="left", padx=10)

        language_names = sorted(self.translator_app.language_mapping)
        self.language_var = ctk.StringVar(value="English")
        self.language_menu = ctk.CTkOptionMenu(
            self.language_frame,
            variable=self.language_var,
            values=language_names,
        )
        self.language_menu.pack(side="left", padx=10)

    def handle_voice_input(self):
        text = self.translator_app.speech_to_text()
        if text:
            self.text_box.delete("1.0", "end")
            self.text_box.insert("1.0", text)
            self.translated_label.configure(text="")
        else:
            self.translated_label.configure(text="No speech was recognized.")

    def handle_translation(self):
        text = self.text_box.get("1.0", "end").strip()
        if not text:
            self.translated_label.configure(text="Enter or speak some text first.")
            return

        target_language = self.translator_app.language_mapping[self.language_var.get()]
        translated = self.translator_app.translate_text(text, target_language)
        self.translated_label.configure(text=translated)

if __name__ == "__main__":
    app = TranslatorAppGUI(translatorApp())
    app.mainloop()