from personCreator import *
import random
import generatorUtility as util
import os

def plotSelector():
    motivePath = os.path.join(os.path.dirname(__file__), "plots", "motives.txt")
    actionPath = os.path.join(os.path.dirname(__file__), "plots", "actupon.txt")
    motive = lambda:util.selectFromFile(motivePath)
    action = lambda:util.selectFromFile(actionPath)
    charList = ["Alice","Bob","Casey"]
    mover = "Alice" # nameSelector(genderSelector())  # mover as in an Aristotle type way
    movee = "Bob" # nameSelector(genderSelector())
    event = " ".join([mover,action(),movee]) #,"because",motive()]) 
    reaction = " ".join(["and",movee,action(),mover]) 

    eventList = []
    for i in range(3):
        mover = random.choice(charList)
        listWithoutMover = charList[:]
        listWithoutMover.remove(mover)
        movee = random.choice(listWithoutMover)
        event = " ".join([mover,action(),movee])
        if random.randint(0,1):
            l = event.split()
            l.insert(1,traitSelector().lower() + "ly")
            event = " ".join(l)
        eventList.append(event)

    if random.randint(0,1):
        l = event.split()
        l.insert(1,traitSelector().lower() + "ly")
        event = " ".join(l)
    if random.randint(0,1):
        l = reaction.split()
        l.insert(2,traitSelector().lower() + "ly")
        reaction = " ".join(l)
    moverTraits = " ".join(["Alice is",traitSelector().lower()])
    moveeTraits = " ".join(["Bob is",traitSelector().lower()])
    return "\n".join(eventList) + "\n"
    #return "\n".join([moverTraits,moveeTraits,"",event,reaction]) + "\n"
    #return "\n".join([event,reaction]) + "\n"
