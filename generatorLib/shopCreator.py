import generatorUtility as util

def weaponSelector():
    weaponsPath = os.path.join(os.path.dirname(__file__), "items", "weapons.txt")
    return util.selectFromFile(weaponsPath)
