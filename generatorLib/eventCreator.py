from .generatorUtility import selectFromFile
import os

def eventSelector():
    eventsPath = os.path.join(os.path.dirname(__file__), "events", "events.txt")
    return selectFromFile(eventsPath)
