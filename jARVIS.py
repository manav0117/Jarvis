import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
#print(voices[1].id)
def speak(audio): #Function for making the jarvis speak
    engine.say(audio)
    engine.runAndWait()
def wishMe(): #Function for wishing the user according to the time
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good Morning ")
    elif(hour>=12 and hour<18):
        speak("Good Afternoon ")
    else:
        speak("Good Evening ")
def takeCommand(): #Function that takes microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=0.8
       # r.energy_threshold=400
        audio=r.listen(source)
    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print("User said : ",query)
    except Exception as e:
       # print(e)
         print("Say that again please....")
         #speak("Say that again please")
         return "None"
    return query

speak("I am your personal assistant Jarvis. Tell me how can i help you.")
if __name__ == '__main__':
   wishMe()
   while True:
       query=takeCommand().lower()
       #Logic for executing task based on query
       if 'wikipedia' in query:
           speak("Searching Wikipedia...")
           query=query.replace("wikipedia","")
           results=wikipedia.summary(query,sentences=2)
           speak("According to wikipedia")
           speak(results)
       elif 'open youtube' in query:
           webbrowser.open("youtube.com")
       elif 'open google' in query:
           webbrowser.open("google.com")