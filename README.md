# Desktop Assistant

Desktop Assistant is a command-line Python-based desktop assistant. It provides various functionalities to assist you with tasks on your computer.

## Features

### Music Player
You can play music by specifying the path to a directory containing MP3 files. Supported music commands include:
- `play music`
- `play some music`
- `play a song`

The assistant will play a random song from the specified folder.

### Website Launcher
You can open websites using specific commands. Currently, only websites listed in the `sites_list` dictionary can be opened. To launch a site, use commands like:
- `Open youtube`
- `Open github`

You can customize the list of supported websites by editing the `sites_list` dictionary in the code.

### Reminders
Set reminders with ease. Say or type "Set reminder" or "Set a reminder," and a window will prompt you to specify the reminder message and the number of minutes from now when the reminder should trigger. Be sure to enter a numeric value for the time. The reminder window's "Set" button should close the window, but manual closure may be required.

### App Launcher
Launch applications using simple commands. Supported applications include:
- Calculator
- Mail
- Windows Photo Viewer

You can add more applications by modifying the `applicationlauncher` function in the code.Head over to the applicationlauncher function, add an elif statement, put the command of your choice, and specify the path of the application within os.startfile(). This should allow you to open ypur custom apps through voice or text input.

### Conversational AI
Engage in natural language conversations and generate text, stories, or code using the Palm API. To use this feature, you'll need a valid API key.
Without an API key you can still access the other features.

## Further Plans
- Develop a graphical user interface (UI) for a more user-friendly interaction.
- Optimize the website launching feature to support opening any website by command.
- Add the ability to play specific songs by their names.
- Enhance command flexibility and usability.

## Requirements
- Python
- Necessary Python libraries (e.g., pyttsx3, requests)
- Palm API key (for conversational AI)
