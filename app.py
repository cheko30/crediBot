from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
import playsound
import speech_recognition as sr
from gtts import gTTS
import random

app = Flask(__name__)

credi_bot = ChatBot(
    "CrediBot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri='sqlite:///database.sqlite3'
)

trainer = ChatterBotCorpusTrainer(credi_bot)
trainer.train(
    "./data/creditos.yml"
)

trainer.export_for_training('./traning.json')


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(credi_bot.get_response(userText))
    # return speak(str(daliaBot.get_response(userText)))


def speak(text):
    tts = gTTS(text=text, lang="es")
    numero = random.randint(1, 9)
    filename = "voice" + str(numero) + ".mp3"
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


if __name__ == "__main__":
    app.run()
