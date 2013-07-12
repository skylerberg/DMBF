from panes import CharacterPane, StatsPane, WeatherPane, TownPane, InnPane, EventPane
from Tkinter import Menu
import sys

mainPane = None

def addMenuBar(root, pane):
    global mainPane
    mainPane = pane
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Character Generator", command=lambda:launchCharacter(root,mainPane))
    filemenu.add_command(label="Weather Generator", command=lambda:launchWeather(root,mainPane))
    filemenu.add_command(label="Town Generator", command=lambda:launchTown(root,mainPane))
    filemenu.add_command(label="Inn Generator", command=lambda:launchInn(root,mainPane))
    filemenu.add_command(label="Event Generator", command=lambda:launchEvent(root,mainPane))
    filemenu.add_command(label="Statistics Mode", command=lambda:launchStats(root,mainPane))
    menubar.add_cascade(label="File",menu=filemenu)
    root.config(menu=menubar)

def clearPane(currentPane): #must be called by any function that creates a pane
    print ("NEW WINDOW")
    currentPane.frame.grid_forget()
    currentPane.frame.destroy()

def launchCharacter(master,currentPane):
    clearPane(currentPane)
    readPoint = sys.stdout.tell()
    global mainPane
    mainPane = CharacterPane(master, readPoint)

def launchStats(master,currentPane):
    clearPane(currentPane)
    readPoint = sys.stdout.tell()
    global mainPane
    mainPane = StatsPane(master,readPoint)

def launchWeather(master,currentPane):
    clearPane(currentPane)
    readPoint = sys.stdout.tell()
    global mainPane
    mainPane = WeatherPane(master,readPoint)

def launchTown(master,currentPane):
    clearPane(currentPane)
    readPoint = sys.stdout.tell()
    global mainPane
    mainPane = TownPane(master,readPoint)

def launchInn(master,currentPane):
    clearPane(currentPane)
    readPoint = sys.stdout.tell()
    global mainPane
    mainPane = InnPane(master,readPoint)

def launchEvent(master,currentPane):
    clearPane(currentPane)
    readPoint = sys.stdout.tell()
    global mainPane
    mainPane = EventPane(master,readPoint)