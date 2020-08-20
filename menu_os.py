import os
import getpass
name=getpass.getuser()                                            #To get the name of the user from the current account
from datetime import datetime                                     #To get current date and time
print(f"WELCOME TO WINDOWS {name}",end="")
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("\t\t\t\t\t\t\t\tDate and Time :", dt_string)
print(f"\n\nHello , I am here for you {name} ,(To turn me off please enter CTRL + C )")
done = "Wait,launching in a second........"
while True:                                                     #Loop to ask the user infinite time ,till he interrupt

    user = input("\nPlease ask me what can i do for you : ")
    todo = user.lower()
    if "dont" in todo or "do not " in todo :                              #Checking whether anything mentioned not to do
        print("OK ,Tell me the next command .")
    elif "open" in todo or "launch" in todo or "run" in todo or "zoom" in todo or "want" in todo or "play" in todo:
        if "magnifier" in todo or "zoom" in todo or "enlarge" in todo:          #check command for Magnifier
            print(done)
            os.system("magnify")
        elif "system" in todo or "configuration" in todo or "details" in todo:  #check command for system configuration
            print(done)
            os.system("msconfig")
        elif "computer" in todo or "pc" in todo or "file" in todo:              #Check command for files
            print(done)
            os.system("explorer")
        elif "wordpad" in todo or "wordeditor" in todo or "write" in todo:      #Check command for wordpad
            print(done)
            os.system("write")
        elif "calculator" in todo or "calculate" in todo:                       #Check command for calculator
            print(done)
            os.system("calc")
        elif "chrome" in todo or "browse" in todo or "google" in todo:          #Check command for chrome
            print(done)
            os.system("chrome")
        elif "note" in todo or "editor" in todo or "plain" in todo:             #Check command for notepad
            print(done)
            os.system("notepad")
        elif "draw" in todo or "paint" in todo or "art" in todo :               #Check command for MS-paint
            print(done)
            os.system("mspaint")
        elif "music" in todo or "media" in todo or "player" in todo or "song" in todo:  #Check command for W M Player
            print(done)
            os.system("wmplayer")
        else:
            print("Please enter something valid ")
    else:
        print("Please give me a valid command")




