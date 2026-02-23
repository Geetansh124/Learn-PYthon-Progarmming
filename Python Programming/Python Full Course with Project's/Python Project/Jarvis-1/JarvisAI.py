import win32com.client

def say(text):
    os.system(f'say {text}')

speaker = win32com.client.Dispatch("SAPI.SpVoice")


if __name__ == "__main__":
    print('PyCharm')
    say("Hello I am Jarvis A.I")
    while True:
        print("Listening...")
        speaker.Speak(s)
        query = takeCommand()
        say(query)

while 1:
    print("Enter the word you want to speak it out by computer")
    s = input()
    speaker.Speak(s)
