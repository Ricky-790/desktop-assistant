#IMPORTS
from plyer import notification
import time
import google.generativeai as palm
import speech_recognition as sr
import os
import pyttsx3
import threading
import pygame
import mutagen.mp3
import random
import webbrowser
from tkinter import *
#set palm api-key
palm.configure(api_key="Your API_KEY")

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
        os.startfile('calc.exe')
        return 1
    elif query in('launch gallery','launch photos'):
        os.startfile('ms-photos:')
        return 1
    elif query in ('launch email','launch mail'):
        os.startfile('mailto:') #will open your default mail app
        return 1
    elif query=='launch discord':
        os.startfile("C:\\Users\\wwwri\\Desktop\\Discord.lnk") #Path to the discord shortcut. You can add your preffered apps to open on command like this.
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
    reminder_win.destroy()
    title = titlebox.get()
    delay = int(time_box.get())
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
    
defaults = {
  'model': 'models/chat-bison-001',
  'temperature': 0.6,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
}
context = "Stella is an AI chat assistant designed to assist users with various tasks and provide information through text-based conversations. Stella is designed to be concise, direct, and to the point in her responses, and seeks to avoid extraneous information or language that distracts from the task at hand. Stella's creators believe that concise, clear, and focused responses improve the user experience and help users accomplish their goals quickly and efficiently."
examples = []
messages = []
file='chathistory.txt' ##Your previous messages throughout all sessions will be stored in the file chathistory.txt. This is optional and you can remove it if you want
with open(file,'r') as f:
    past_messages=f.read()
    past_messages=past_messages.replace('[','')
    past_messages=past_messages.replace(']','')
    past_messages=past_messages.replace('\'','')
    past_messages=past_messages.replace('"','')
    past_messages=past_messages.split(',')
    for i in past_messages:
        messages.append(i)
    f.close()
def chat(query):
    messages.append(query)
    response = palm.chat(
      **defaults,
      context=context,
      examples=examples,
      messages=messages
    )
    print(f'Assistant:{response.last}')
    engine.say(response.last)
    engine.runAndWait()

time_object = time.localtime()
localtime = time.strftime('%H', time_object)
localtime=int(localtime)
if localtime>=5 and localtime<12:
    engine.say('Good Morning!')
    engine.runAndWait()
elif localtime>=12 and localtime<18:
    engine.say('Good Afternoon!')
    engine.runAndWait()
else:
    engine.say('Good Evening!')
    engine.runAndWait()


while True:
    
    query=input('You: ')
    if(query=='openmic'): #Type openmic after launching the program to give voice command.
        commandinput()

    s=0
    a=0
    r=0
    s=OpenBrowser(query)
    a=AppLauncher(query)
    r=reminder_set(query)
    if s==1 or a==1 or r==1:
        continue
    elif query in ('play music','play some music','play a song'):
        engine.say('Playing a song from your library')
        engine.runAndWait()
        music_thread = threading.Thread(target=PlayMusic)
        music_thread.start()
    else:
        chat(query)
        with open (file,'w') as f:
            f.write(str(messages))
            f.close()
