from panes import *
from Tkinter import Menu
import sys

mainPane = None

def addMenuBar(root, pane):
    global mainPane
    mainPane = pane
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Character Generator", command=lambda:launchPane(root,mainPane,CharacterPane))
    filemenu.add_command(label="Weather Generator", command=lambda:launchPane(root,mainPane,WeatherPane))
    filemenu.add_command(label="Town Generator", command=lambda:launchPane(root,mainPane,TownPane))
    filemenu.add_command(label="Inn Generator", command=lambda:launchPane(root,mainPane,InnPane))
    filemenu.add_command(label="Event Generator", command=lambda:launchPane(root,mainPane,EventPane))
    filemenu.add_command(label="Plot Generator", command=lambda:launchPane(root,mainPane,PlotPane))
    filemenu.add_command(label="Statistics Mode", command=lambda:launchPane(root,mainPane,StatsPane))
    menubar.add_cascade(label="File",menu=filemenu)
    root.config(menu=menubar)

def clearPane(currentPane): #must be called by any function that creates a pane
    print ("NEW WINDOW")
    currentPane.frame.grid_forget()
    currentPane.frame.destroy()

def launchPane(master,currentPane,newPaneType):
    clearPane(currentPane)
    readPoint = sys.stdout.tell()
    global mainPane
    mainPane = newPaneType(master, readPoint)
