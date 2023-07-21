import random
from .generatorUtility import selectFromFile
import os

def nameSelector():
    typeSeedInt = random.randint(1,7)
    nounPath = os.path.join(os.path.dirname(__file__), "taverns", "tavernNouns.txt")
    descriptorPath = os.path.join(os.path.dirname(__file__), "taverns" , "tavernDescriptors.txt")

    if typeSeedInt <= 1: #The NOUN and NOUN
        firstNounStr = selectFromFile(nounPath)
        secondNounStr = selectFromFile(nounPath)
        while firstNounStr == secondNounStr:
            secondNounStr = selectFromFile(nounPath)
        return "The " + firstNounStr + " and " +  secondNounStr

    elif typeSeedInt <= 2: #The DESCRIPTOR NOUN and DESCRIPTOR NOUN
        firstNounStr = selectFromFile(nounPath)
        secondNounStr = selectFromFile(nounPath)
        firstDescriptorStr = selectFromFile(descriptorPath)
        secondDescriptorStr = selectFromFile(descriptorPath)
        while firstNounStr == secondNounStr:
            secondNounStr = selectFromFile(nounPath)
        while firstDescriptorStr == secondDescriptorStr:
            secondDescriptorStr = selectFromFile(descriptorPath)
        return "The " + firstDescriptorStr + " " + firstNounStr + " and " + secondDescriptorStr + " " + secondNounStr

    elif typeSeedInt <= 3: #The DESCRIPTOR NOUN and NOUN
        firstNounStr = selectFromFile(nounPath)
        secondNounStr = selectFromFile(nounPath)
        descriptorStr = selectFromFile(descriptorPath)
        while firstNounStr == secondNounStr:
            secondNounStr = selectFromFile(nounPath)
        return "The " + descriptorStr + " " + firstNounStr + " and " + secondNounStr

    elif typeSeedInt <= 4: #The NOUN and DESCRIPTOR NOUN
        firstNounStr = selectFromFile(nounPath)
        secondNounStr = selectFromFile(nounPath)
        descriptorStr = selectFromFile(descriptorPath)
        while firstNounStr == secondNounStr:
            secondNounStr = selectFromFile(nounPath)
        return "The " + firstNounStr + " and " + descriptorStr + " " + secondNounStr

    elif typeSeedInt <= 5: #The NOUN
        nounStr = selectFromFile(nounPath)
        return "The " + nounStr

    elif typeSeedInt <= 6: #The DESCRIPTOR Inn
        descriptorStr = selectFromFile(descriptorPath)
        return "The " + descriptorStr + " Inn "

    elif typeSeedInt <= 7: #The DESCRIPTOR NOUN
        nounStr = selectFromFile(nounPath)
        descriptorStr = selectFromFile(descriptorPath)
        return "The " + descriptorStr + " " + nounStr
