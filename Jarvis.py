from gtts import gTTS
import speech_recognition as sr
import os
import re
import webbrowser
import smtplib
import requests
import pyttsx3

engine=pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()

def talk(audio):
    "speaks audio passed as argument"

    print(audio)
    tts=gTTS(text=audio,lang='en')
    tts.save('audio.mp3')
    os.system("mpg123 audio.mp3")

    
            

def myCommand(): #Listens for the command

    r=sr.Recognizer() #Recognize the microphone as source

    with sr.Microphone() as source:
        print("Ready...")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source, duration=1) #Helps block out outside noise
        audio=r.listen(source)

    try:
        command=r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    except sr.UnknownValueError:
        print("Unable to understand you")
        assistant(myCommand())
    return command

def assistant(command): #Exectuing commands
    if 'open Reddit python' in command:
        print("hi")
    if "Hi":
        talk("Hello")
talk("I am ready for your command")

while True:
    assistant(myCommand())
    
