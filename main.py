import speech_recognition as sr
import pyttsx3
import sounddevice as sd
from scipy.io.wavfile import write
from deep_translator import GoogleTranslator
def speak(text, language="en"):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    if voices:
        engine.setProperty('voice', voices[0].id)
        engine.say(text)
        engine.runAndWait()
def speech_to_text():
    fs = 16000
    seconds = 5
    print(" Please speak now in English...")
    recording = sd.rec(int (seconds * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    recognizer = sr.Recognizer()
    recognizer = sr.Recognizer()
    with sr.AudioFile("temp.wav") as source:
        audio = recognizer.record(source)
    try:
