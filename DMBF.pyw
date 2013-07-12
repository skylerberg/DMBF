from graphics.panes import CharacterPane
from graphics.menu import addMenuBar
from Tkinter import Tk
import sys

##Clear logs, and redirect output to files
sys.stdout = open("sessionlog.txt","w+",0)
sys.stderr = open("errorlog.txt","w+",0)

#Initialize main frame, title program, start with character generator, initializes read point
root = Tk()
root.wm_title("Dungeon Master's Best Friend")
readPoint = 0
currentPane = CharacterPane(root, readPoint)

#Main Menu Bar
addMenuBar(root, currentPane)

root.mainloop()
sys.stdout.close()
sys.stderr.close()
