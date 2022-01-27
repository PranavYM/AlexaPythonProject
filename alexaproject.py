import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser
import datetime

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command
while True:
    def run_alexa():
        command = take_command()
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'what is a' and 'what is an' and 'who is' and 'who is a' and 'who is an' and 'tell me about' in command:
            person = command.replace('what is', '').replace('who is', '').replace('tell me about', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk('According to Wikipedia' + info)

        elif 'search for' in command:
            statement = command.replace('search for', '')
            talk('searching for' + statement + 'via google')
            pywhatkit.search(statement)
        
        elif 'open youtube' in command:
            talk('opening youtube')
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in command:
            talk('opening google')
            webbrowser.open("https://www.google.com/")

        elif 'open prime video' in command:
            talk('opening prime video')
            webbrowser.open("https://www.primevideo.com")

        elif 'open netflix' in command:
            talk('opening netflix')
            webbrowser.open("https://www.netflix.com/")

        elif 'open weather channel' in command:
            talk('opening weather channel')
            webbrowser.open("https://weather.com/")
            
        elif 'what is the time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)

        else:
            talk('Sorry please try again later.')
        exit()
    run_alexa()
