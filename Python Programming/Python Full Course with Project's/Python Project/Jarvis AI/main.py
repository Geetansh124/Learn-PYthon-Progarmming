import os

#import win32com.client
import speech_recognition as sr




def say(text):
    os.system(f"say{text}")

#speaker = win32com.client.Dispatch("SAPI.SpVoice")



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
        return query


if __name__ == '__main__':
    print("Welcome to Speech Recognition")
    say("Hello I am Jarvis A.I")
    print("Listening...")
    text = takeCommand()
    say(text)
    

#while 1:
    #print("Enter the world you want to speak it out by computer")
    #s = input()
