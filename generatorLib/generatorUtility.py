import random

def selectFromFile(path):
    with open(path) as f:
        dataList = list(f)
    if dataList[0].find(":") != -1:  # if there is a colon in the first line of the file
        weightedDict = dictionaryCreator(dataList)  # assume it is a raffle dictionary
        return weightedSample(weightedDict)
    else:
        return random.choice(dataList).strip()  # otherwise return a randomly chosen line

def dictionaryCreator(formattedList):
    dictionary = dict()
    for line in formattedList:
       key, value = line.split(":")
       key = key.strip()
       value = int(value.strip())
       dictionary[key] = value #takes each line and enters it into the dictionary
    return dictionary

def weightedSample(weightedDictionary):
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
