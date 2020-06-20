import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init()


def speak(audio):
    # text to speech
    engine.say(audio)
    # wait till speech end
    engine.runAndWait()

# speak("Hello sagar This is  Jarvis How may i help you")
# time function


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

# date function


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak(day)
    speak(month)
    speak(year)


def wishme():
    speak("Hello this is jarvis, welcome back sagar ")
    speak("Current date is ")
    date()
    speak("and current time is ")
    time()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("so Good morning sir")
    elif hour >= 12 and hour < 18:
        speak("so Good aftenoon sir")
    elif hour >= 18 and hour < 24:
        speak("so Good Evening sir")
    else:
        speak("so good night Sir")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recongnizning...")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return query 
takeCommand()