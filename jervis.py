import pyttsx3
import datetime
import speechRecognition as sr
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('vioces')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishme():

    hour = int(datetime.datetime.now().hour)    
    if hour>=0 and hour<12:
        speak("good morning")

    elif hour>=12 and hour<4:
        speak("good afternoon")

    elif hour>4 and hour<6:
        speak("good Evening!")
    speak("I am jarvis Sir .please tell me how may I help you?")


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
        # print(e)    
        print("Say that again please...")   
    return query
if __name__ == "__main__":
    wishme()
    while True:
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if wikipedia in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")   

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))  

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")  

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
    def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
elif 'email to harry' in query:
    try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
    except Exception as e:
        print(e)
speak("Sorry my friend harry bhai. I am not able to send this email") 

import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib