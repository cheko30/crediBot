import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS


def speak(text):
    tts = gTTS(text=text, lang="es")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio, language="en")
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said


text = get_audio()
if "hello" in text:
    speak("hello, how are you!")

if "what is your name" in text:
    speak("My name is DaliaBot")

#speak("Hola a todos y bienvenidos")
#get_audio()

'''r = sr.Recognizer()

with sr.Microphone() as source:
    print('Speak Anything : ')
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print('You said: {}'.format(text))
    except:
        print('Sorry could not hear')
'''
