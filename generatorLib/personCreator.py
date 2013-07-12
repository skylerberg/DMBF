import random
import generatorUtility as util
import os

def genderSelector():
    if random.randint(0,1):
        return "male"
    else:
        return "female"

def nameSelector(gender="male"):
    try:
        name = ""
        if gender == "male":
            maleNames = util.listCreator(open(os.path.dirname(__file__) + "/names/maleFirst.txt"))
            name += str(maleNames[random.randint(0,len(maleNames)-1)])
        else:
            femaleNames = util.listCreator(open(os.path.dirname(__file__) + "/names/femaleFirst.txt"))
            name += str(femaleNames[random.randint(0,len(femaleNames)-1)])
        name += " "
        lastNames = util.listCreator(open(os.path.dirname(__file__) + "/names/last.txt"))
        name += str(lastNames[random.randint(0,len(lastNames)-1)])
        return name
    except (IndexError):
        print "!!!Index error in nameSelector!!!"
        print '!!!Make sure gender != ""!!!'
        return "UNABLE TO GENERATE NAME"

def occupationTypeSelector(excludedOccupationTypes = set(),setting="urban"):
    allOccupationTypes = util.dictionaryCreator(open(os.path.dirname(__file__) + "/occupations/typesList" + setting.capitalize() + ".txt"))
    allowedOccupationTypes = dict()
    for occType in allOccupationTypes:
        if occType not in excludedOccupationTypes:
            allowedOccupationTypes[occType] = allOccupationTypes[occType]
    return util.weightedSample(allowedOccupationTypes)

def occupationSelector(occupationType="default"):
    if occupationType == "default":
        occupationType = occupationTypeSelector()
    try:
        occupationWeight = util.dictionaryCreator(open(os.path.dirname(__file__) + "/occupations/"+occupationType+".txt"))
    except(IOError, TypeError):
        print ("ERROR: unable to understand occupation type " + occupationType)
        return "no occupation"
    return util.weightedSample(occupationWeight)

def eyeColorSelector():
    return util.weightedSample(util.dictionaryCreator(open(os.path.dirname(__file__) + "/eyes/eyeColor.txt")))

def hairColorSelector(eyecolor):
    return util.weightedSample(util.dictionaryCreator(open(os.path.dirname(__file__) + "/hair/"+eyecolor+"EyesHair.txt")))

def hairTypeSelector():
    return util.weightedSample(util.dictionaryCreator(open(os.path.dirname(__file__) + "/hair/hairTypes.txt")))

def hairLengthSelector():
    return util.weightedSample(util.dictionaryCreator(open(os.path.dirname(__file__) + "/hair/hairLengths.txt")))

def traitSelector():
    return random.sample(util.listCreator(open(os.path.dirname(__file__) + "/traits/traits.txt")),1)[0]

def ageSelector(ageType):
    age = 0
    if ageType == "normal":
        for roll in range(0,random.randint(5,8)):
            age += random.randint(1,6)
    if ageType == "old":
        for roll in range(0,random.randint(15,20)):
            age += random.randint(1,6)
    return age
