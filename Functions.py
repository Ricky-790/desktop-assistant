#IMPORTS
from plyer import notification
import time
import speech_recognition as sr
import os
import pyttsx3
import threading
import pygame
import mutagen.mp3
import random
import webbrowser
from tkinter import *


# Create a pyttsx3 engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)#(0 for male voice or 1 for female voice)
engine.rate=1
#Function to take input Via Mic
def commandinput():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
        voicecom=r.recognize_google(audio,language='en-in')
        voicecom=voicecom.lower()
        print(f'You: {voicecom}')
        return voicecom

song_names=os.listdir("C:\\Users\\wwwri\\Music\\") #Specify your local music directory path here. Make sure only mp3 files are present in the folder, or it might produce an error while trying to play

#Function to play music
def PlayMusic():
    song=random.choice(song_names)
    music_file =("C:\\Users\\wwwri\\Music\\"+song)
    print(f'playing: {song}')
    duration = mutagen.mp3.MP3(music_file).info.length * 60
    pygame.init()
    # Play the music file "my_music.mp3"
    pygame.mixer.music.load(music_file)
    # Play the music
    pygame.mixer.music.play()
    time.sleep(duration)

#list the site name, along woth their .com or .net or .to
sites_list = {
    "youtube": "com",
    "github": "com",
    "aniwatch": "to",
    "google": "com",
    "vyvymanga": "net"
}
def OpenBrowser(query):
    query=query.lower()
    for i in sites_list:
        if query==(f'Open {i}').lower():
            print(f'Opening {i}....')
            engine.say(f'opening {i}')
            engine.runAndWait()
            webbrowser.open(f'https://{i}.{sites_list[i]}')
            return 1
        


def AppLauncher(query):
    query=query.lower()
    if query=='launch calculator':
        print('Lia: Right away...')
        engine.say('Right away')
        engine.runAndWait()
        os.startfile('calc.exe')
        return 1
    elif query in('launch gallery','launch photos'):
        print('Lia: Right away...')
        engine.say('Right away')
        engine.runAndWait()
        os.startfile('ms-photos:')
        return 1
    elif query in ('launch email','launch mail'):
        print('Lia: Right away...')
        engine.say('Right away')
        engine.runAndWait()
        os.startfile('mailto:') #will open your default mail app
        return 1
    elif query=='launch discord':
        print('Lia: Right away...')
        engine.say('Right away')
        engine.runAndWait()
        os.startfile("C:\\Users\\User\\Desktop\\Discord.lnk") #Path to the discord shortcut. You can add your preffered apps to open on command like this.
    else:
        return 0

def reminder_set(query):
    query=query.lower()
    if query in('set a reminder','set reminder'):
        global reminder_win
        reminder_win =Tk()
        reminder_win.title('Set Reminder')
        reminder_win.geometry('500x300')
        reminder_win.config(background='#1f3138')
        label=Label(reminder_win,text='Set Reminder',font=('Ink free',24),bg='white', fg='blue',)
        label.place(x=160,y=0)
        title=Label(reminder_win,text='Title to notify',font=('Arial', 18))
        title.place(x=0,y=50)
        global titlebox
        titlebox=Entry(width=25,font=('Arial', 16))
        titlebox.place(x=180,y=50)

        time_label=Label(reminder_win,text='How many\nminutes later?\n(Enter a number)',font=('Arial', 14))
        time_label.place(x=0,y=170)
        global time_box
        time_box=Entry(width=25,font=('Arial', 14))
        time_box.place(x=180,y=170)

        submit_button = Button(reminder_win, text='Set',font=('Arial',14),bg='#3277a8',fg='white',relief=None,highlightthickness=2, highlightbackground="black",command=submit)
        submit_button.place(x=235,y=240)
        return 1

def submit():
    title = titlebox.get()
    delay = int(time_box.get())
    reminder_win.destroy()
    print(f'Lia: Reminder set for {title}, {delay} minutes from now.')
    delay=delay*60
    notification_thread = threading.Thread(target=sendnotif,args=(title,delay))
    notification_thread.start()

def sendnotif(notiftitle,delay):
    time.sleep(delay)
    notification.notify(
        title=notiftitle,
        message='You set a reminder',
        timeout=5
    )
    

time_object = time.localtime()
localtime = time.strftime('%H', time_object)
localtime=int(localtime)
def greet():
    if localtime>=5 and localtime<12:
        engine.say('Good Morning!')
        engine.runAndWait()
    elif localtime>=12 and localtime<18:
        engine.say('Good Afternoon!')
        engine.runAndWait()
    else:
        engine.say('Good Evening!')
        engine.runAndWait()