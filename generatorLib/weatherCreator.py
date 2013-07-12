import random
import os
import generatorUtility as util

UNDEFINED = "UNDEFINED"

def weatherSelector(season="winter",yesterday=UNDEFINED):
    if yesterday != UNDEFINED:    #If a previous weather is provided there is a 50% chance it will be the same today
        if random.randint(0,1):
            return yesterday
    return util.weightedSample(util.dictionaryCreator(open(os.path.dirname(__file__) + "/weather/"+season+".txt")))
