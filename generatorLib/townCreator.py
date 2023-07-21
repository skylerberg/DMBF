import random
import os
from .generatorUtility import selectFromFile

def nameSelector():
    townNamesPath = os.path.join(os.path.dirname(__file__), "towns", "townNames.txt")
    return selectFromFile(townNamesPath)

def infastructureSelector(popK): #popK == population in thousands
    #In infrastructureRarities.txt the number represents the number of people expected to support an establishment
    rarityPath = os.path.join(os.path.dirname(__file__), "towns", "infrastructureRarities.txt")
    with open(rarityPath) as f:
        modifierDict = util.dictionaryCreator(list(f))
    infastructureDict = dict()
    for establishmentType in modifierDict:
        rarity = modifierDict[establishmentType]
        mu = (popK*1000)/float(rarity)
        sigma = mu*.50 #stadard deviation as a % of mu is arbitrary
        roll = int(round(random.gauss(mu,sigma)))
        if roll < 0:
            roll = 0 #No negative values for amount of infrastructure
        infastructureDict[establishmentType] = roll
    return infastructureDict
