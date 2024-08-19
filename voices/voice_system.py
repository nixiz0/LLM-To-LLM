import pyttsx3
import os
from constant.colors import *
from voices.visual_voice_system import VisualSyntheticVoice


class NarratorVoice:
    def __init__(self, voice_color):
        self.voice_color = voice_color

        # Initialize the text-to-speech engine
        self.engine = pyttsx3.init()

        # Obtain the list of available voices
        voices = self.engine.getProperty('voices')

        # Show all available voices
        for i, voice in enumerate(voices):
            print(f"{i}. {voice.name} ({voice.languages})")

        while True:
            try:
                # Ask the user to choose a voice
                voice_id = int(input(f"{BLUE}Choose a voice number: {RESET}"))
                if 0 <= voice_id < len(voices):
                    self.chosen_voice = voices[voice_id].id
                    break
                else:
                    print(f"{RED}Please enter a valid voice number.{RESET}")
            except ValueError:
                print(f"{RED}Please enter a valid integer.{RESET}")
                
    def speak(self, text):
        # Set narrator voice
        self.engine.setProperty('voice', self.chosen_voice)

        # Create the directories if they don't exist
        directory = "voices/temp_output_voice/"
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Create the full file path
        full_path = os.path.join(directory, "voice_output.wav")

        # If the file already exists, remove it
        if os.path.exists(full_path):
            os.remove(full_path)

        # Convert text to speech and save it to a file
        self.engine.save_to_file(text, full_path)

        # Wait for any pending speech to complete
        self.engine.runAndWait()

        # Create an instance of the class and call the play_audio method
        visual_voice = VisualSyntheticVoice(voice_color=self.voice_color)
        visual_voice.play_audio(filename=full_path)