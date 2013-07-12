import random
import generatorUtility as util
import os

def nameSelector():
    typeSeedInt = random.randint(1,7)

    if typeSeedInt <= 1: #The NOUN and NOUN
        nounList = util.listCreator(open(os.path.dirname(__file__) + "/taverns/tavernNouns.txt"))
        firstNounStr = str(nounList[random.randint(0,len(nounList)-1)])
        secondNounStr = str(nounList[random.randint(0,len(nounList)-1)])
        while firstNounStr == secondNounStr:
            secondNounStr = str(nounList[random.randint(0,len(nounList)-1)])
        return "The " + firstNounStr + " and " +  secondNounStr

    elif typeSeedInt <= 2: #The DESCRIPTOR NOUN and DESCRIPTOR NOUN
        nounList = util.listCreator(open(os.path.dirname(__file__) + "/taverns/tavernNouns.txt"))
        descriptorList =  util.listCreator(open(os.path.dirname(__file__) + "/taverns/tavernDescriptors.txt"))
        firstNounStr = str(nounList[random.randint(0,len(nounList)-1)])
        secondNounStr = str(nounList[random.randint(0,len(nounList)-1)])
        firstDescriptorStr = str(descriptorList[random.randint(0,len(descriptorList)-1)])
        secondDescriptorStr = str(descriptorList[random.randint(0,len(descriptorList)-1)])
        while firstNounStr == secondNounStr:
            secondNounStr = str(nounList[random.randint(0,len(nounList)-1)])
        while firstDescriptorStr == secondDescriptorStr:
            secondDescriptorStr = str(descriptorList[random.randint(0,len(descriptorList)-1)])
        return "The " + firstDescriptorStr + " " + firstNounStr + " and " + secondDescriptorStr + " " + secondNounStr

    elif typeSeedInt <= 3: #The DESCRIPTOR NOUN and NOUN
        nounList = util.listCreator(open(os.path.dirname(__file__) + "/taverns/tavernNouns.txt"))
        descriptorList =  util.listCreator(open(os.path.dirname(__file__) + "/taverns/tavernDescriptors.txt"))
        firstNounStr = str(nounList[random.randint(0,len(nounList)-1)])
        secondNounStr = str(nounList[random.randint(0,len(nounList)-1)])
        descriptorStr = str(descriptorList[random.randint(0,len(descriptorList)-1)])
        while firstNounStr == secondNounStr:
            secondNounStr = str(nounList[random.randint(0,len(nounList)-1)])
        return "The " + descriptorStr + " " + firstNounStr + " and " + secondNounStr

    elif typeSeedInt <= 4: #The NOUN and DESCRIPTOR NOUN
        nounList = util.listCreator(open(os.path.dirname(__file__) + "/taverns/tavernNouns.txt"))
        descriptorList =  util.listCreator(open(os.path.dirname(__file__) + "/taverns/tavernDescriptors.txt"))
        firstNounStr = str(nounList[random.randint(0,len(nounList)-1)])
        secondNounStr = str(nounList[random.randint(0,len(nounList)-1)])
        descriptorStr = str(descriptorList[random.randint(0,len(descriptorList)-1)])
        while firstNounStr == secondNounStr:
            secondNounStr = str(nounList[random.randint(0,len(nounList)-1)])
        return "The " + firstNounStr + " and " + descriptorStr + " " + secondNounStr

    elif typeSeedInt <= 5: #The NOUN
        nounList = util.listCreator(open(os.path.dirname(__file__) + "/taverns/tavernNouns.txt"))
        nounStr = str(nounList[random.randint(0,len(nounList)-1)])
        return "The " + nounStr

    elif typeSeedInt <= 6: #The DESCRIPTOR Inn
        descriptorList =  util.listCreator(open(os.path.dirname(__file__) + "/taverns/tavernDescriptors.txt"))
        descriptorStr = str(descriptorList[random.randint(0,len(descriptorList)-1)])
        return "The " + descriptorStr + " Inn "

    elif typeSeedInt <= 7: #The DESCRIPTOR NOUN
        nounList = util.listCreator(open(os.path.dirname(__file__) + "/taverns/tavernNouns.txt"))
        descriptorList =  util.listCreator(open(os.path.dirname(__file__) + "/taverns/tavernDescriptors.txt"))
        nounStr = str(nounList[random.randint(0,len(nounList)-1)])
        descriptorStr = str(descriptorList[random.randint(0,len(descriptorList)-1)])
        return "The " + descriptorStr + " " + nounStr
