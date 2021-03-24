import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and  hour<12:
        speak("good morning boss")
    elif hour>=12 and hour<18:
        speak("good afternoon boss")
    else:
        print("good evening boss")
    speak(" i Am jarvis ! how may i help you")

def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening................")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
         print("Recognising...")
         query = r.recognize_google(audio,language='en-in')
         print(f"user said: {query}\n")
    except Exception as e:
        print("say this again.....")
        return "none"
    return query


if __name__ =="__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak("Searching wikipedia....")
            query=query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            speak("according to wikipeida")
            print(result)
            speak(result)
        elif "you" in query:
            speak("i am good boss! it is depend on you how to take care of me. you are a god for me")
            break
        elif "exam" in query:
            speak("boss today is your design and analysis of algorithm exam.")
            break
        elif "tommorow" in query:
            speak("forget about it boss! just enjoy your day")
            break
        elif "jarvis open youtube" in query:
            speak("opening youtube sir!")
            webbrowser.open("youtube.com")

        elif "hey jarvis what is the time" in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strtime}")

