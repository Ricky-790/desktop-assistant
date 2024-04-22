import customtkinter as ct
from PIL import Image as Im
from Functions import *
import Gemini_api as gp
import time


n=0
z=0

def speak(response):
    border_label.place(x=135, y=6)
    engine.say(response)
    engine.runAndWait()
    border_label.place_forget()

def post_msg(query, sender):
    global z
    if sender=='user':
        ct.CTkLabel(master=screen,font=('Helvetica', 15) ,text=f'{query}',corner_radius=15, fg_color='#65B741',text_color='white', wraplength=420).pack(anchor='e', pady=n)
        z=1
    if sender=='lia':
        ct.CTkLabel(master=screen,font=('Helvetica', 15), text=f'{query}',corner_radius=15, fg_color='#6420AA',text_color='white', wraplength=350).pack(anchor='w', pady=n)

def send_message():
    global n
    global z
    query=Entrybox.get()
    def call_gp_chat():
        response = gp.chat(query)
        response=response.replace('*', '')
        post_msg(response, 'lia')
        # print(f'Lia : {response}')
                
        speech_thread = threading.Thread(target=lambda:speak(response))
        speech_thread.start()
    if not query.strip():
        Entrybox.delete(0, END)
        return
    Entrybox.delete(0, END)
    post_msg(query, 'user')
    if z==1:
        z=0
        n+=10
        s=0
        a=0
        r=0
        s=OpenBrowser(query)
        a=AppLauncher(query)
        r=reminder_set(query)
        if s==1 or a==1 or r==1:
            pass
        elif query in ('play music','play some music','play a song'):
            engine.say('Playing a song from your library')
            engine.runAndWait()
            border_label.destroy()
            music_thread = threading.Thread(target=PlayMusic)
            music_thread.start()
        else:
            threading.Thread(target=call_gp_chat).start()
            
        

    # border_label.place(x=135, y=13)

    #chat(prompt)

    
    


win = ct.CTk()
win.title('Lia')
win.geometry('450x500')

border_image = Im.open("greencircle.png")  # Replace with your image path
border_image = border_image.resize((180, 180))  # Resize the image to fit the frame
border_image = ct.CTkImage(light_image=border_image, dark_image=border_image, size=(180,180))
border_label = ct.CTkLabel(master=win, image=border_image, text='')


image = Im.open("Lia.png")  # Replace with your image path
image = image.resize((150, 150))  # Resize the image to fit the frame
image = ct.CTkImage(light_image=image, dark_image=image, size=(150,150))

image_label = ct.CTkLabel(master=win, image=image, text='')
image_label.place(x=150, y=20)

name_label = ct.CTkLabel(master=win, text='Lia', font=('Arial',18))
name_label.place(x=215,y=182)

screen = ct.CTkScrollableFrame(master=win,
                            width=420,
                            height=38,
                            fg_color='#121111',
                            border_width=0.6,
                            border_color='#FFFFDD'
                            )
screen.place(x=5, y=210)

Entrybox = ct.CTkEntry(master=win,
                 width = 350,
                 height = 40,
                 border_width=0.7,
                 border_color='white',
                 corner_radius=30,
                 placeholder_text='Message...',
                 fg_color='#FFEAE3',
                 text_color='black'
                 )

Entrybox.place(x=15, y=450)

send_button = ct.CTkButton(master=win,
                                 width=60,
                                 height=40,
                                 border_width=0.7,
                                 border_color='white',
                                 corner_radius=30,
                                 text="Send",
                                 command=send_message,
                                 text_color='white',
                                 fg_color='#074173',
                                 hover_color='#1679AB'
                                 )
send_button.place(x=370, y=450)

line_label = ct.CTkLabel(master=win,text='',font=('Arial',1), width=500, height=0.05, fg_color='white')
line_label.place(y=430)

greet()
win.mainloop()