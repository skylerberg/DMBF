import generatorUtility as util

def weaponSelector():
    return util.weightedSample(util.dictionaryCreator(open("items/weapons.txt")))
