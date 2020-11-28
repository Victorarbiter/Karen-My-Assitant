import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import requests
import os
import sys


engine = pyttsx3.init('sapi5')

rate = engine.getProperty('rate')
volume = engine.getProperty('volume')
voice = engine.getProperty('voice')

newVoiceRate = 150
engine.setProperty('rate', newVoiceRate)
newVoice = 10
engine.setProperty('voice', newVoice)
newVoiceVolume = 0.9
engine.setProperty('volume', newVoiceVolume)

client = wolframalpha.Client('JW6y7Q-GKWVR76AJG')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH <=18:
        speak('Good Evening!')
    if currentH >= 19 and currentH > 18:
        speak('Good Night!')

greetMe()

speak('Hello Sir.')
speak('How may I help you?')


def myCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en')
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query


if __name__ == '__main__':

    while True:

        query = myCommand();
        query = query.lower()

        if 'open youtube' in query:
            speak('opening!')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('opening!')
            webbrowser.open('www.google.com')

        elif 'open gmail' in query:
            speak('Opening!')
            webbrowser.open('www.gmail.com')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'do you have a joke' in query:
            res = requests.get(
                    'https://icanhazdadjoke.com/',
                    headers={"Accept":"application/json"}
                    )
            if res.status_code == requests.codes.ok:
                speak(str(res.json()['joke']))
            else:
                speak('oops!I ran out of jokes')

        elif 'hahaha that funny' in query:
            speak('i want to tell you sir, that i love to see you happy.')

        elif 'open browser' in query:
            speak('opening!')
            webbrowser.open('https://weboas.is/')

        elif 'cyber map' in query:
            speak('processing!')
            webbrowser.open('https://cybermap.kaspersky.com/')


        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()

                    server = smtplib.SMTP('YOUR_EMAIL', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("YOUR_USERNAME", 'YOUR_PASSWORD')
                    server.sendmail('SUBJECT', "RECIPIENT", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif 'open weather' in query:
            speak('opening')
            webbrowser.open('https://go.init.st/jta2aa9')

        elif 'hello' in query:
            speak('Hello Sir.')

        elif 'goodbye' in query:
            speak('have a good day sir.')
            sys.exit()

        elif 'drop my needle' in query:
            music_folder = 'D:\\'
            music = ['Jingle-Bells']
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)

            speak('')

        elif 'wake up' in query:
            music_folder = 'D:\\'
            music = ['Wake-up']
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)

            speak('well hello Sir!')

        elif 'back to hardware mode' in query:
            music_folder = 'D:\\'
            music = ['Hardware']
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)

            speak('Lets do it!')


        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('Got it.')
                    speak(results)

                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak(results)

            except:
                webbrowser.open('www.google.com')

    #    speak('Next Command! Sir!')
