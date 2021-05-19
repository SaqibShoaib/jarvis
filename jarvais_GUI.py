from tkinter import *
import tkinter.messagebox as tmsg
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


root = Tk()
root.iconbitmap("jar_icon.ico")
root.title("Jarvais")
root.geometry("720x780")
root.maxsize(720,780)
root.minsize(720,780)

def clear(fr):
    for widget in fr.winfo_children():
        widget.destroy()
    fr.destroy()
# __________Password Portion starts Here

# def check_pass():
#     password = "saqib234"
#     if password == c_pass.get():
#         tmsg.showinfo("Attention","Click ok to proceed")
#         f.destroy()
#     else:
#         ck = tmsg.askretrycancel("Attention","Press retry to enter password again and cancel to exit.")
#         if ck:
#             clear(f)
#             ident()
#         else:
#             quit()   
# f = Frame(root,relief=SUNKEN,padx=50,pady=50)
# f.pack(pady=200)
# c_pass = StringVar()
# def ident():
#     Label(f,text="Enter Password Please",font=("shadows into light",15)).pack()
#     Entry(f,textvariable=c_pass,font=("times new roman",12)).pack(ipadx=5,ipady=5)
#     Button(f,text="Submit",command=check_pass).pack(pady=5)
# ident()

# _______________Password Identifier ends here
# def wishMe():
#     hour = int(datetime.datetime.now().hour)
#     if hour > 0 and hour < 12 : 
#         speak("Hello Saqib Good Morning") 
#     elif hour >= 12 and hour < 18 : 
#         speak("Hello Saqib Good Afternoon") 
#     else: 
#         speak("Hello Saqib Good Evening") 
#     speak("I am Your PC assistant, How can I help You")
# def bye():
#     speak("Take care Good bye shakib")
#     sys.exit()
f2 = Frame(root,relief=SUNKEN,padx=50,pady=50)
f2.pack(pady=200,fill="both")

# f3 = Frame(root,borderwidth=2)
# f3.pack(pady=200)
# take command function

# def takecomand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         r.pause_threshold = 1
#         mylabel = Label(f3,text="Listining..")
#         mylabel.pack()       
#         audio = r.listen(source)
#     try:
#         Label(f3,text="Recognizing...").pack()
#         query = r.recognize_google(audio, language='en-us') #Using google for voice recognition.
#         Label(f3,text=f"User Said: {query}").pack()  #User query will be printed.
#     except Exception as e:
#         # print(e)    
#         print("Kindly speak again")
#         return "None" #None string will be returned
#     return query


# take command function ends here
# voice fun starts from here
# def voice_fun():
#     clear(f2)
#     wishMe()
#     Label(f3,text="Welcome From Voice Assistant",
#     font=("shadows into light",15)).pack()
#     Button(f3,text="Click Here to search",command=takecomand).pack()

# text mode function starts form here
music_dir = 'C:\\Users\\Muhammad Saqib\\Music'
def text_fun():
    global sr_google
    global sr_youtube
    global sr_wikipedia
    global sr_stackoverflow
    clear(f2)
    col = Frame(root,borderwidth=2)
    col.pack(side=LEFT,anchor="nw")
    # search labels
    Label(col,text="Search on Google: ",font=("Times new roman",12)).pack(pady=50,padx=15)
    Label(col,text="Search on YouTube: ",font=("Times new roman",12)).pack(pady=50,padx=18)
    Label(col,text="Search on Wikipedia: ",font=("Times new roman",12)).pack(pady=50,padx=20)
    Label(col,text="Search on Stackoverflow: ",font=("Times new roman",12)).pack(pady=50,padx=20)
    col2= Frame(root,borderwidth=2)
    col2.pack(side=LEFT,anchor="nw")
    # variables
    sr_google = StringVar()
    sr_youtube = StringVar()
    sr_wikipedia = StringVar()
    sr_stackoverflow = StringVar()
    # entries
    Entry(col2,font=("times new roman",12),textvariable=sr_google,width=20).pack(pady=50,ipady=1)
    Entry(col2,font=("times new roman",12),textvariable=sr_youtube,width=20).pack(pady=50,ipady=1)
    Entry(col2,font=("times new roman",12),textvariable=sr_wikipedia,width=20).pack(pady=50,ipady=1)
    Entry(col2,font=("times new roman",12),textvariable=sr_stackoverflow,width=20).pack(pady=50,ipady=1)
    col3 = Frame(root,borderwidth=2)
    col3.pack(side=LEFT,anchor="nw")
    # search buttons
    Button(col3,text="Search",command=search_on_google,font=("times new roman",10)).pack(pady=47,padx=20)
    Button(col3,text="Search",command=search_on_youtube,font=("times new roman",10)).pack(pady=47,padx=20)
    Button(col3,text="Search",command=search_on_wikipedia,font=("times new roman",10)).pack(pady=47,padx=20)
    Button(col3,text="Search",command=search_on_stackoverflow,font=("times new roman",10)).pack(pady=47,padx=20)
    #  buttons in col 1
    Button(col,text="Open Gmail",command=open_gmail,font=("times new roman",10),padx=5,pady=5).pack(pady=10)
    Button(col,text="Open Udemy",command=open_udemy,font=("times new roman",10),padx=5,pady=5).pack(pady=10)
    Button(col,text="Open Meetings",command=open_meet,font=("times new roman",10),padx=5,pady=5).pack(pady=10)
    Button(col,text="Open whatsapp",command=open_whatsapp,font=("times new roman",10),padx=5,pady=5).pack(pady=10)
    # buttons in col 2
    Button(col2,text="Open Code",command=open_vscode,font=("times new roman",10),padx=5,pady=5).pack(pady=15)
    Button(col2,text="Open File",command=open_file,font=("times new roman",10),padx=5,pady=5).pack(pady=15)
    Button(col2,text="Open Cpanel",command=open_cpanel,font=("times new roman",10),padx=5,pady=5).pack(pady=15)
    # buttons in col 3
    Button(col3,text="Play classic music",command = classic_music,font=("times new roman",10),padx=5,pady=5).pack(pady=15,padx=25)
    Button(col3,text="Play my music list",command = myplaylist,font=("times new roman",10),padx=5,pady=5).pack(pady=15,padx=25)
    Button(col3,text="SHUTDOWN PC",command = shutdown,font=("times new roman",10),padx=5,pady=5,bg="red").pack(pady=15,padx=25)

# search on google function
def search_on_google():
    webbrowser.open(f"https://www.google.com/search?q={sr_google.get()}")
# search on Youtube function
def search_on_youtube():
    webbrowser.open(f"https://www.youtube.com/results?search_query={sr_youtube.get()}")
# search on wikipedia function
def search_on_wikipedia():
    result = wikipedia.summary(sr_wikipedia.get() , sentences = 2)
    tmsg.showinfo("Result",result)
# search on stackoverflow function
def search_on_stackoverflow():
    webbrowser.open(f"https://stackoverflow.com/search?q={sr_stackoverflow.get()}")
# open gmail function
def open_gmail():
    webbrowser.open(f"https://mail.google.com/mail/u/1/#inbox")
def open_udemy():
    webbrowser.open(f"https://www.udemy.com/home/my-courses/learning/")
def open_meet():
    webbrowser.open(f"https://mail.google.com/mail/u/1/#calls")
def open_whatsapp():
    webbrowser.open(f"https://web.whatsapp.com/")
def open_vscode():
    codePath = "C:\\Users\\Muhammad Saqib\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(codePath)
def open_file():
    codepath = "C:\\Users\\Muhammad Saqib"
    os.startfile(codepath)
def open_cpanel():
    codepath = "C:\\Users\\Muhammad Saqib\\Desktop\\control panel"
    os.startfile(codepath)
    
def classic_music():
    os.startfile(os.path.join(music_dir, 'playlists\\classic.wpl'))
def myplaylist():
    os.startfile(os.path.join(music_dir, 'playlists\\mylist.wpl'))
def shutdown():
    choice = tmsg.askokcancel("Attentition","Do you really want to turn off pc?")
    if choice:
        os.system("shutdown /s /t 1") 
        quit()
    else:
        return None
# text mode function ends here

# def mode():
#     Label(f2,text="Which mode of jarvais You Want to use",font=("shadows into light",15)).pack()
#     Button(f2,text="Voice Mode",font=("times new roman",12)).pack(side=LEFT,anchor="nw",pady=20,ipadx=20)
#     Button(f2,text="Type Mode",command=text_fun,font=("times new roman",12)).pack(side=RIGHT,anchor="ne",pady=20,ipadx=20)
# mode()
text_fun()
# voice_fun()
root.mainloop()