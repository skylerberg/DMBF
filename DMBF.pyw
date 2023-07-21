from graphics.panes import CharacterPane
from graphics.menu import addMenuBar
from tkinter import Tk
import sys
from contextlib import redirect_stdout, redirect_stderr

##Clear logs, and redirect output to files
# sys.stdout = 
# sys.stderr = open("errorlog.txt","w+",0)

with open("sessionlog.txt","w+") as session_log:
    with open("errorlog.txt","w+") as error_log:
        with redirect_stdout(session_log):
            with redirect_stderr(error_log):
                #Initialize main frame, title program, start with character generator, initializes read point
                root = Tk()
                root.wm_title("Dungeon Master's Best Friend")
                readPoint = 0
                currentPane = CharacterPane(root, readPoint)

                #Main Menu Bar
                addMenuBar(root, currentPane)

                root.mainloop()
