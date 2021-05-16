import os
import pyttsx3
import datetime
import speech_recognition as sr
import smtplib
import wikipedia
import webbrowser
import pywhatkit
import pyautogui

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)





def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#speak("Jarvis here")

def time():

    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is ")
    speak(Time)
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is ")
    speak(date)
    speak(month)
    speak(year)
def wishme():
#    speak("Give me a name.")
#    name = input("Enter the name of your Assistant :")
    speak("Welcome back Black Devil !")
 #   time()
 #   date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <12:

        speak("Good Morning!")
    elif hour >=12 and hour < 18:
        speak("Good Afternoon!")
    elif hour >=18 and hour < 24:
        speak("Good Evening!")
    elif 'open amazon':
        wb.open_new_tab("amazon.in")
    else:
        speak("Good Night !")


    speak("jarvis at your service.")
   # speak(f"{name} at your service!")
    speak("Now! How can I help you")

def screen_shot():
    img = pyautogui.screenshot()
    img.save("D:\PROJECTS\Jarvis\ss\sh.png")



def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again,  sir !")
        return "None"
    return query


if __name__ == '__main__':
    wishme()
    while True:
        query = takecommand().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=4)
            print(result)
            speak(result)
        elif 'play songs' in query:
            songs_dir = 'D:\ABHINASH\MUSIC'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif 'play on youtube' in query:
            speak("What should I play? sir! ")
            query = takecommand().lower().replace('play on youtube', '')
            print("playing..." + query)
            pywhatkit.playonyt(query)
        elif 'remember that' in query:
            speak("what ?")
            data = takecommand()
            speak("you said me to remember that" + data)
            remember = open('remember file.txt', 'w')
            remember.write(data)
            remember.close()
        elif 'what did i asked you to remember' in query:
            remember = open("remember file.txt", 'r')
            speak("You said me to remember that " + remember.read())
        elif 'screenshot' in query:
            screen_shot()
            speak("Done!")


        elif 'offline' in query:
            quit()

















