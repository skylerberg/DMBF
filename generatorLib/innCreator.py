import random
import generatorUtility as util
import os

def nameSelector():
    typeSeedInt = random.randint(1,7)
    nounPath = os.path.join(os.path.dirname(__file__), "taverns", "tavernNouns.txt")
    descriptorPath = os.path.join(os.path.dirname(__file__), "taverns" , "tavernDescriptors.txt")

    if typeSeedInt <= 1: #The NOUN and NOUN
        firstNounStr = util.selectFromFile(nounPath)
        secondNounStr = util.selectFromFile(nounPath)
        while firstNounStr == secondNounStr:
            secondNounStr = util.selectFromFile(nounPath)
        return "The " + firstNounStr + " and " +  secondNounStr

    elif typeSeedInt <= 2: #The DESCRIPTOR NOUN and DESCRIPTOR NOUN
        firstNounStr = util.selectFromFile(nounPath)
        secondNounStr = util.selectFromFile(nounPath)
        firstDescriptorStr = util.selectFromFile(descriptorPath)
        secondDescriptorStr = util.selectFromFile(descriptorPath)
        while firstNounStr == secondNounStr:
            secondNounStr = util.selectFromFile(nounPath)
        while firstDescriptorStr == secondDescriptorStr:
            secondDescriptorStr = util.selectFromFile(descriptorPath)
        return "The " + firstDescriptorStr + " " + firstNounStr + " and " + secondDescriptorStr + " " + secondNounStr

    elif typeSeedInt <= 3: #The DESCRIPTOR NOUN and NOUN
        firstNounStr = util.selectFromFile(nounPath)
        secondNounStr = util.selectFromFile(nounPath)
        descriptorStr = util.selectFromFile(descriptorPath)
        while firstNounStr == secondNounStr:
            secondNounStr = util.selectFromFile(nounPath)
        return "The " + descriptorStr + " " + firstNounStr + " and " + secondNounStr

    elif typeSeedInt <= 4: #The NOUN and DESCRIPTOR NOUN
        firstNounStr = util.selectFromFile(nounPath)
        secondNounStr = util.selectFromFile(nounPath)
        descriptorStr = util.selectFromFile(descriptorPath)
        while firstNounStr == secondNounStr:
            secondNounStr = util.selectFromFile(nounPath)
        return "The " + firstNounStr + " and " + descriptorStr + " " + secondNounStr

    elif typeSeedInt <= 5: #The NOUN
        nounStr = util.selectFromFile(nounPath)
        return "The " + nounStr

    elif typeSeedInt <= 6: #The DESCRIPTOR Inn
        descriptorStr = util.selectFromFile(descriptorPath)
        return "The " + descriptorStr + " Inn "

    elif typeSeedInt <= 7: #The DESCRIPTOR NOUN
        nounStr = util.selectFromFile(nounPath)
        descriptorStr = util.selectFromFile(descriptorPath)
        return "The " + descriptorStr + " " + nounStr
