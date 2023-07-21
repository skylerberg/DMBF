import random
from .generatorUtility import selectFromFile
import os

DEFAULT = "default"

def genderSelector():
    if random.randint(0,1):
        return "male"
    else:
        return "female"

def nameSelector(gender="male"):
    name = ""
    if gender == "male":
        maleNamesPath = os.path.join(os.path.dirname(__file__), "names", "maleFirst.txt")
        name += selectFromFile(maleNamesPath)
    else:
        femaleNamesPath = os.path.join(os.path.dirname(__file__), "names", "femaleFirst.txt")
        name += selectFromFile(femaleNamesPath)
    name += " "
    lastNamesPath = os.path.join(os.path.dirname(__file__), "names", "last.txt")
    name += selectFromFile(lastNamesPath)
    return name

def occupationTypeSelector(excluded=None,setting="urban"):
    settingFileName = "typesList" + setting.capitalize() + ".txt"
    occupationTypesPath = os.path.join(os.path.dirname(__file__), "occupations", settingFileName)
    retVal = selectFromFile(occupationTypesPath)
    if retVal == excluded:  # if we get the excluded value, try again
        return occupationTypeSelector(excluded,setting)
    return retVal

def occupationSelector(occupationType=DEFAULT):
    if occupationType == DEFAULT:
        occupationType = occupationTypeSelector()
    occupationPath = os.path.join(os.path.dirname(__file__), "occupations", occupationType + ".txt")
    return selectFromFile(occupationPath)

def eyeColorSelector():
    eyeColorPath = os.path.join(os.path.dirname(__file__), "eyes", "eyeColor.txt")
    return selectFromFile(eyeColorPath)

def hairColorSelector(eyecolor):
    hairColorPath = os.path.join(os.path.dirname(__file__), "hair", eyecolor + "EyesHair.txt")
    return selectFromFile(hairColorPath)

def hairTypeSelector():
    hairTypePath = os.path.join(os.path.dirname(__file__), "hair", "hairTypes.txt")
    return selectFromFile(hairTypePath)

def hairLengthSelector():
    hairLengthsPath = os.path.join(os.path.dirname(__file__), "hair", "hairLengths.txt")
    return selectFromFile(hairLengthsPath)

def traitSelector():
    traitsPath = os.path.join(os.path.dirname(__file__), "traits", "traits.txt")
    return selectFromFile(traitsPath)

def ageSelector(ageType):
    age = 0
    if ageType == "normal":
        for roll in range(0,random.randint(5,8)):
            age += random.randint(1,6)
    if ageType == "old":
        for roll in range(0,random.randint(15,20)):
            age += random.randint(1,6)
    return age
