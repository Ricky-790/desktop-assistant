from Functions import *
import Gemini_api as gp

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
        response = gp.chat(query)
        print(f'Lia : {response}')
        engine.say(response)
        engine.runAndWait()
        
