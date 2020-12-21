from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import pyttsx3
import pymsgbox
import os


def talk(text):
    engine.say(text)
    engine.runAndWait()


Trans = Translator()
engine = pyttsx3.init()
voice_id = engine.getProperty('voices')
engine.setProperty('rate', 150)
engine.setProperty('voice', voice_id[1].id)
r = sr.Recognizer()
mic = sr.Microphone()
talk("Hello")
talk("Welcome to the smart translator")


def translator():
    talk("Please give the destination language")
    with mic as source:
        talk("listening")
        print("Listening")
        r.adjust_for_ambient_noise(source)
        audio2 = r.listen(source)
        talk("Recognizing")
        print("recognizing")
    try:
        lang1 = r.recognize_google(audio2)
    except:
        talk("Sorry we could not get the destination language")
        talk("Please Enter the destination language")
        lang1 = pymsgbox.password(text="Enter the destination language(lower)", title="Please enter the text here",
                                  default="", mask=None)
    talk('recognized')
    print("recognized")
    dt1 = Trans.detect(str(lang1))
    if dt1.lang != 'en':
        lang2 = Trans.translate(lang1, dest='en')
    else:
        lang2 = lang1
    talk("Please tell me what do i need to translate")
    with mic as source:
        talk("listening")
        print("Listening")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        print("Recognizing")
        talk("Recognizing")
    try:
        text1 = r.recognize_google(audio)
    except:
        talk("sorry we could not get the sentence")
        talk("Please enter the text in box")
        text1 = pymsgbox.password(text="Enter the text to be translated", title="Please enter the text here",
                                  default="",
                                  mask=None)
    talk("Translating")
    text2 = Trans.translate(text1, dest=lang2)
    my_obj: gTTS = gTTS(text2.text, lang=text2.dest, slow=False)
    my_obj.save("welcome.mp3")
    talk("Translated")
    playsound("welcome.mp3")
    os.remove("welcome.mp3")


def allow():
    talk("Do I need to translate something else?")
    with mic as source:
        talk("listening")
        print("Listening")
        r.adjust_for_ambient_noise(source)
        audio3 = r.listen(source)
        print("Recognizing")
        talk("Recognizing")
    confirm1 = r.recognize_google(audio3)
    return confirm1


def confirm():
    text = allow()
    if 'yes' in text:
        translator()
        confirm()
    elif 'no' in text:
        talk("Thank you so much")
        talk("we hope you had a good experience")


translator()
confirm()


