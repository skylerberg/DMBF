from generatorLib import personCreator

class Character(object):
    def __init__(self,name="random",gender="random",age="normal",setting="urban",allowCoastal="disallow"):
        if gender == "random":
            self.gender = personCreator.genderSelector()
        else:
            self.gender = gender
        if name == "random":
            self.name = personCreator.nameSelector(self.gender)
        else:
            self.name = name
        self.age = personCreator.ageSelector(age)
        if allowCoastal == "allow":
            self.occupation = personCreator.occupationSelector(personCreator.occupationTypeSelector(setting=setting))
        else:
            self.occupation = personCreator.occupationSelector(personCreator.occupationTypeSelector("coastal",setting))
        self.eyeColor = personCreator.eyeColorSelector()
        self.hairColor = personCreator.hairColorSelector(self.eyeColor)
        self.hairType = personCreator.hairTypeSelector()
        self.hairLength = personCreator.hairLengthSelector()
        self.trait1 = personCreator.traitSelector()
        self.trait2 = personCreator.traitSelector()
        self.trait3 = personCreator.traitSelector()

    def output(self):
        print (self.name + ":")
        print (self.gender.capitalize())
        print ("Age: " + str(self.age))
        print ("Occupation: " + self.occupation.capitalize())
        print ("Appearance:")
        print ("\t" + self.hairLength.capitalize()+ ", " + self.hairType + ", " + self.hairColor + " hair")
        print ("\t" + self.eyeColor.capitalize() + " eyes")
        print ("Traits:")
        print ("\t" + self.trait1)
        print ("\t" + self.trait2)
        print ("")
