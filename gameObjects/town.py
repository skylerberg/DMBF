from generatorLib import townCreator

class Town(object):
    def __init__(self,popK):
        self.name = townCreator.nameSelector()
        self.infastructureDict = townCreator.infastructureSelector(popK)

    def output(self):
        print(self.name + ":")
        templist = []
        for item in self.infastructureDict:
            templist.append(item + ":" + str(self.infastructureDict[item]))
        templist.sort()
        for item in templist:
            print(item)
        print("")
