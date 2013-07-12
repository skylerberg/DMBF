import random
import generatorUtility as util
import os

def eventSelector():
    return random.sample(util.listCreator(open(os.path.dirname(__file__) + "/events/events.txt")),1)[0]
