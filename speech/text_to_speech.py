import pyttsx3
from config.settings import SPEECH_RATE

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', SPEECH_RATE)
    engine.say(text)
    engine.runAndWait()