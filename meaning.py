from nltk.corpus import wordnet
import pyttsx3
import speech_recognition as sr
import pymsgbox


def talk(text1):
    eng.say(text1)
    eng.runAndWait()


def speech():
    with mic as source:
        talk("Listening")
        print("listening")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        talk("recognizing")
        print('recognizing')
    return audio


r = sr.Recognizer()
mic = sr.Microphone()
eng = pyttsx3.init()
voices = eng.getProperty('voices')
eng.setProperty('rate', 160)
eng.setProperty('volume', 0.7)
eng.setProperty('voice', voices[1].id)
talk("Welcome to the smart dictionary")


def meanings():
    talk("Please tell me the word you wish to know the meaning of")
    audio1 = speech()
    try:
        txt = r.recognize_google(audio1)
    except :
        talk("Sorry , I could not get the word")
        talk("Please Enter the text in box")
        txt = pymsgbox.password(text="Enter the word here", title="Alternate input", default='',
                                mask=None)
    text = txt
    talk("recognized")
    print("recognized")
    syn = wordnet.synsets(text)
    print("definition of ", text, "is")
    print(syn[0].definition())
    print(syn[0].examples())
    talk("The definition of " + text + "is")
    talk(syn[0].definition())
    talk("examples")
    talk(syn[0].examples())


def allow():
    talk("Do you wish to know the meaning of any other word?")
    audio2 = speech()
    text2 = r.recognize_google(audio2)
    return text2


def confirm():
    text3 = allow()
    if 'yes' in text3:
        meanings()
        confirm()
    if 'no' in text3:
        talk("Thank you so much")
        talk("I hope you had a good experience")
        exit()
    else:
        talk("Invalid Input")
        talk("Input must have a yes or no in it")
        confirm()


meanings()
confirm()
