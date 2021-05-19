import pyttsx3
import datetime
import sys
import wikipedia 
import speech_recognition as sr
import webbrowser
import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)
newVoiceRate = 145
engine.setProperty('rate',newVoiceRate)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12 : 
        speak("Hello Saqib Good Morning") 
    elif hour >= 12 and hour < 18 : 
        speak("Hello Saqib Good Afternoon") 
    else: 
        speak("Hello Saqib Good Evening") 
    speak("I am Your PC assistant, How can I help You")

def takecomand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-us') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.
    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query
def identifeir():
    speak("Password Please")
    password = takecomand()
    while not (password == "Alpha" or password=="alpha" or password == "sakib" or password == "Shakib" or password == "Saqib"):
        speak("Wrong Password Kindly speak Again")
        password = takecomand()
    return wishMe()
def runagain():
    speak("if you want to enter another command type YES or want to quit me then Enter bye?")
    choice = input("Enter your choice: ")
    choice = choice.lower()
    if choice == "yes":
        return
    else:
        return bye()



def bye():
    speak("Take care Good bye shakib")
    sys.exit()
if __name__=="__main__" :
    music_dir = 'C:\\Users\\Muhammad Saqib\\Music'
    code_dir = 'C:\\Users\\Muhammad Saqib\\AppData\\Local\\Programs\\Microsoft VS Code'
    identifeir()
    while True:
        speak("Enter command please")
        query = takecomand().lower()
        if query == "quit" or query == "bye":
            bye()
            
        if 'wikipedia' in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia"," ")
            result = wikipedia.summary(query , sentences = 2)
            print(result)
            speak("Accodding To Wikipedia")
            speak(result)
        if 'open youtube' in query:
            speak(f"opening youtube")
            webbrowser.open(f"https://www.youtube.com/")
        if query == 'open gmail' or query == 'check inbox':
            speak(f"opening gmail")
            webbrowser.open(f"https://mail.google.com/mail/u/1/#inbox")
        if query == 'check meetings' or query == 'check calls':
            speak(f"checking calls")
            webbrowser.open(f"https://mail.google.com/mail/u/1/#calls")
        if 'open google' in query:
            speak(f"opening google")
            webbrowser.open(f"https://www.google.com/")
        if 'open whatsapp' in query:
            speak(f"opening whatsapp")
            webbrowser.open(f"https://web.whatsapp.com/")
        if ('open udemy' or 'open my courses' )in query:
            speak(f"opening udemy")
            webbrowser.open(f"https://www.udemy.com/home/my-courses/learning/")
        if ('open stackoverflow' or 'open stack overflow') in query:
            speak(f"opening stackoverflow")
            webbrowser.open(f"https://www.stackoverflow.com/")
        if query == 'what time it is' or query == 'time please':
            time = datetime.datetime.now().strftime("%I:%M:%S:%p")
            time = time.replace(':',"")
            speak(f"The time right now is {time}")
        if 'on youtube' in query:
            query = query.replace("on youtube"," ")
            speak(f"searching {query} on youtube")
            query.replace(" ","+")
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        if 'on google' in query:
            query = query.replace("on google"," ")
            speak(f"searching {query} on google")
            query.replace(" ","+")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        if ('on stack overflow' or 'on stackoverflow') in query:
            query = query.replace("on stack overflow"," ")
            speak(f"searching {query} on stackoverflow")
            query.replace(" ","+")
            webbrowser.open(f"https://stackoverflow.com/search?q={query}")
        if (query == 'play classic music' or query == 'play classic playlist' or query == 'play classic song'):
            os.startfile(os.path.join(music_dir, 'playlists\\classic.wpl'))
        if (query == 'play my music' or query == 'play my list' or query == 'play my playlist' or query == 'play my songs'):
            os.startfile(os.path.join(music_dir, 'playlists\\mylist.wpl'))
        
        if (query == 'open code' or query == 'open vscode' or query == 'open text editor' or query == 'open ide'):
            codePath = "C:\\Users\\Muhammad Saqib\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        if (query == "who are you"):
            speak("I am Desktop assistant")
        if (query == 'hello how are you' or query == 'hello' or query =='how are you'):
            speak("i am fine and healthy. hope you are fine and healthy too")
        
        if (query == 'shutdown' or query == 'shutdown pc' or query == 'shut down'):
            speak("Do you really want to turn off your device?")
            print("Do you really want to turn off your device?")
            choice = takecomand().lower()
            if choice == 'yes':
                os.system("shutdown /s /t 1") 
                bye()
                
        runagain()