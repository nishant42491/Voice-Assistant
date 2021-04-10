from django.shortcuts import render

from django.http import HttpResponse

import speech_recognition as sr

import datetime


from time import sleep

import pyjokes as pyjokes



from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import pprint
import webbrowser

import os
import wikipedia

import pyttsx3



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

def VoiceAssistantInput(request):


    class _TTS:

        def __init__(self):
            self.engine = pyttsx3.init()
            

        def speak(self,audio):
            self.engine.say(audio)
            self.engine.runAndWait()
            
        
        
        


    def greetme():
        
        hour = int(datetime.datetime.now().hour)
        if 0 <= hour < 12:
            tts=_TTS()
            tts.speak("Good Morning Sir !")
            del(tts)

        elif 12 <= hour < 18:
            tts=_TTS()
            tts.speak("Good Afternoon Sir !")
            del(tts)
            

        else:
            tts=_TTS()
            tts.speak("Good Evening Sir !")
            del(tts)

        assistant_name = "zed"
        tts=_TTS()
        tts.speak("hello my name is ")    
        tts.speak(assistant_name)
        tts.speak('how may i help you ')
        del(tts)



    tts=_TTS()
    def takeCommand():
        r = sr.Recognizer()

        with sr.Microphone() as source:

            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            print(e)
            print("Unable to Recognize your voice.")
            return "None"

        return query


    
    clear = lambda: os.system('cls')

        # This Function will clean any
        # command before execution of this python file
    clear()
    greetme()

    
        

    query = takeCommand().lower()
           

    if 'wikipedia' in query:
                # searching stuff in wikipedia
        tts.speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        try:
            results = wikipedia.summary(query, sentences=2)
            tts.speak("According to Wikipedia")
            print(results)
            tts.speak(results)
        except:
                tts.speak('cant find wikipedia page')

    elif 'open youtube' in query:
                tts.speak("Here you go to Youtube\n")
                webbrowser.open("youtube.com")

    elif 'open google' in query:
                tts.speak("Here you go to Google\n")
                webbrowser.open("google.com")

    elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                tts.speak(f"Sir, the time is {strTime}")

    elif 'how are you' in query:
                tts.speak("I am fine, Thank you")

    elif 'joke' in query:
                tts.speak(pyjokes.get_joke())

    elif 'video' in query:
                tts.speak('taking you to youtube')
                webbrowser.open('youtube.com')

    elif 'music' or 'song' in query:
                tts.speak('redirecting to spotify')
                webbrowser.open('spotify.com')


    elif 'exit' in query:
                tts.speak("Thanks for giving me your time")
                exit()
                
    del(tts)


    return render(request,'voiceassistant.html')

        

   

        




'''def VoiceAssistantInput(request):
    r=sr.Recognizer()

    with sr.Microphone() as source :
        
        audio=r.listen(source)
        
        try:
            text= r.recognize_google(audio)
            return HttpResponse('you are saying:{}'.format(text))
            
            
        except :
            return HttpResponse('you are saying nothing')'''
        
