import random

def dictionaryCreator(formattedFile):
    dictionary = dict()
    for line in formattedFile:
       key, value = line.split(":")
       key = key.strip()
       value = int(value.strip())
       dictionary[key] = value #takes each line and enters it into the dictionary
    formattedFile.close()
    return dictionary

def listCreator(formattedFile):
    newList = []
    for line in formattedFile:
        newList.append(line.strip("\n"))
    formattedFile.close()
    return newList

def weightedSample(weightedDictionary,):
    # works like a raffle
    numberOfEntries = 0
    for item in weightedDictionary: #takes each key from dictionary and adds it to a list value number of times
        numberOfEntries += weightedDictionary[item]
    roll = random.randint(1,numberOfEntries)
    selected = "Default"
    for item in weightedDictionary:
        roll -= weightedDictionary[item]
        if roll <= 1:
            selected = item
            break
    return selected
