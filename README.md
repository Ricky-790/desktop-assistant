# desktop-assistant
A desktop assistant (which runs on your terminal for now) created using python

Features:
Can play Music. You need to specify the path to your directory containing the mp3 files. As of now, no controls such as next or previous have been added. The commands that can play music are: ['play music','play some music','play a song']. This will play a random song from the specified folder.
Can open websites from your command. For now, only the websites that are mentioned in sites_list dictionary in the code, can be opened. Looking to optimise it so any website can be opened by command. Currently, you need to type/say "Open youtube" or "Open github", and the site will be launched. You can add sites you want by editing the sites_list dictionary.
Can set reminders. Write or say "Set reminder" or "Set a reminder", and a window will pop up, asking for what you need to be reminded of, and how many minutes from now. Enter your desired information, to get a notification alert on time. Please put a number in the time field for this, or it might run into an error (since I did not add a try-except statement where i should have.) Clicking the "Set" button on the reminder window should close the wwindow, but it is not working for some reason. Close that window manually, and you will get a notification on time
Can launch apps. You can launch calculator app or open your emails by typing "Launch calculator" or "Launch Mail". As of now, only calculator, mail, and windows photoviewer can be opened with this method. However, you can add your specific applications that you want to launch via command. Head over to the applicationlauncher function, add an elif statement, put the command of your choice, and specify the path of the application within os.startfile(). This should allow you to open ypur custom apps through voice or text input
Finally, this assistant can also hold normal conversations, used to generate text/stories or code, thanks to Palm Api. However to use this feature, you will need a palm ai api-key Without an api-key you can still use the other features mentioned above

Further Plans:
To create an UI for interacting with the bot.
Optimising the website launching feature
Adding a feature that will allow user to play a specific song, by saying its name
Making commands more flexible
