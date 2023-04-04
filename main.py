import speech_recognition as sr
import pyaudio

r = sr.Recognizer()

with sr.Microphone(device_index=0) as source:
    print("скажите что нибудь...")
    audio = r.listen(source)

query = r.recognize_google(audio, language="ru-RU")
print ("вы сказали: " + query.lower())
