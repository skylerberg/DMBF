from generatorLib import personCreator
from generatorLib import innCreator
from generatorLib import weatherCreator
from generatorLib import eventCreator
from gameObjects.character import Character
from gameObjects.town import Town
from Tkinter import *

class Pane(object):
    def __init__(self, master, readPoint, mainButtonText):
        self.readPoint = readPoint
        self.frame = Frame(master)
        self.frame.grid()

        self.generate = Button(self.frame,text=mainButtonText,command=self.pressed)
        self.generate.grid(column=0,columnspan=12,row=5,sticky=N+W+E+S)

        self.outputScroll = Scrollbar(self.frame)
        self.output = Text(self.frame,yscrollcommand=self.outputScroll.set)
        self.output.grid(column=0,columnspan=10,row=6,rowspan=10,sticky=S+N+W+E)
        self.outputScroll.grid(column=11,row=6,rowspan=10,sticky=N+S)
        self.outputScroll.config(command=self.output.yview)

    def adjustReadPoint(self):
        sys.stdout.seek(self.readPoint)
        self.output.delete(1.0,END)
        self.output.insert(END,sys.stdout.read())
        self.output.see(END)

    def pressed(self):
        print "Always override pressed and include a call to self.adjustReadPoint"
        self.adjustReadPoint()

class CharacterPane(Pane):

    def __init__(self, master, readPoint):
        super(CharacterPane,self).__init__(master,readPoint,"Generate")

        self.genderMenuTitle = Label(self.frame, text="Gender:")
        self.genderMenuTitle.grid(column=1,row=1)
        self.genderSelected = StringVar()
        self.genderSelected.set("male")
        self.genderRadioMale = Radiobutton(self.frame, text="Male",variable=self.genderSelected,value="male")
        self.genderRadioFemale = Radiobutton(self.frame, text="Female",variable=self.genderSelected,value="female")
        self.genderRadioRandom = Radiobutton(self.frame, text="Random",variable=self.genderSelected,value="random")
        self.genderRadioMale.grid(column=1,row=2)
        self.genderRadioFemale.grid(column=1,row=3)
        self.genderRadioRandom.grid(column=1,row=4)

        self.settingMenuTitle = Label(self.frame,text="Setting:")
        self.settingMenuTitle.grid(column=2,row=1)
        self.settingSelected = StringVar()
        self.settingSelected.set("urban")
        self.settingRadioUrban = Radiobutton(self.frame,text="Urban",variable=self.settingSelected,value="urban")
        self.settingRadioRural = Radiobutton(self.frame,text="Rural",variable=self.settingSelected,value="rural")
        self.settingCoastal = StringVar()
        self.settingCoastal.set("disallow")
        self.settingCheckCoastal = Checkbutton(self.frame,text="Coastal",variable=self.settingCoastal,onvalue="allow",offvalue="disallow")
        self.settingRadioUrban.grid(column=2,row=2)
        self.settingRadioRural.grid(column=2,row=3)
        self.settingCheckCoastal.grid(column=2,row=4)

        self.ageMenuTitle = Label(self.frame,text="Age:")
        self.ageMenuTitle.grid(column=3,row=1)
        self.ageSelected = StringVar()
        self.ageSelected.set("normal")
        self.ageRadioNormal = Radiobutton(self.frame,text="Normal",variable=self.ageSelected,value="normal")
        self.ageRadioOldder = Radiobutton(self.frame,text="Old",variable=self.ageSelected,value="old")
        self.ageRadioNormal.grid(column=3,row=2)
        self.ageRadioOldder.grid(column=3,row=3)

    def pressed(self):
        c = Character(gender=self.genderSelected.get(),age=self.ageSelected.get(),setting=self.settingSelected.get(),allowCoastal=self.settingCoastal.get())
        c.output()
        self.adjustReadPoint()

class StatsPane(Pane):

    def __init__(self, master, readPoint):
        super(StatsPane,self).__init__(master,readPoint,"Tally")

    def populate(self,trait="occupations",sampleSize=10000):
        print ("Generating "+trait+" for a sample size of "+str(sampleSize)+".") ##Loading info
        occurrences = dict()
        if trait == "occupations":
            for iteration in xrange(sampleSize):
                occupation = personCreator.occupationSelector()
                if occupation in occurrences:
                    occurrences[occupation] += 1
                else:
                    occurrences[occupation] = 1
        return occurrences,sampleSize

    def statistics(self,occurrences,sampleSize): ## usually takes *populate() as its arguments
        sortable = []
        for item in occurrences:
            ##sortable.append(item + " " + str(occurances[item])) ##raw numbers
            sortable.append(item + " - " + str(float(occurrences[item])/(sampleSize/100)) + "%") ##percentage
        sortable.sort()
        for line in sortable:
            print (line)

    def pressed(self,):
        self.statistics(*self.populate())
        self.adjustReadPoint()
        self.readPoint = sys.stdout.tell()

class WeatherPane(Pane):

    def __init__(self, master, readPoint):
        super(WeatherPane,self).__init__(master,readPoint,"Generate Day")

        self.seasonMenuTitle = Label(self.frame, text="Season:")
        self.seasonMenuTitle.grid(column=1,row=1)
        self.seasonSelected = StringVar()
        self.seasonSelected.set("winter")
        self.seasonRadioWinter = Radiobutton(self.frame, text="Winter",variable=self.seasonSelected,value="winter")
        self.seasonRadioSpring = Radiobutton(self.frame, text="Spring/Fall",variable=self.seasonSelected,value="spring")
        self.seasonRadioSummer = Radiobutton(self.frame, text="Summer",variable=self.seasonSelected,value="summer")
        self.seasonRadioWinter.grid(column=1,row=2)
        self.seasonRadioSpring.grid(column=1,row=3)
        self.seasonRadioSummer.grid(column=1,row=4)

        self.yesterday="UNDEFINED"

    def pressed(self):
        weather = weatherCreator.weatherSelector(season=self.seasonSelected.get(),yesterday=self.yesterday)
        print weather
        self.yesterday = weather
        self.adjustReadPoint()

class TownPane(Pane):

    def __init__(self, master, readPoint):
        super(TownPane,self).__init__(master,readPoint,"Generate Town")

        self.sizeMenuTitle = Label(self.frame, text="Choose the towns size")
        self.sizeMenuTitle.grid(column=1,row=1)
        self.sizeSelected = IntVar()
        self.sizeSelected.set(1)
        self.sizeRadioHamlet = Radiobutton(self.frame, text="Hamlet (1K)", variable=self.sizeSelected,value=1)
        self.sizeRadioVillage = Radiobutton(self.frame, text="Village (2K)", variable=self.sizeSelected,value=2)
        self.sizeRadioTown = Radiobutton(self.frame, text="Town (5K)", variable=self.sizeSelected,value=5)
        self.sizeRadioCity = Radiobutton(self.frame, text="City (10K)", variable=self.sizeSelected,value=10)
        self.sizeRadioMetropolis = Radiobutton(self.frame, text="Metropolis (35K)", variable=self.sizeSelected,value=35)
        self.sizeSlider = Scale(self.frame,from_=1,to=50,variable=self.sizeSelected,orient=HORIZONTAL,sliderlength=10)
        self.sizeRadioHamlet.grid(column=1,row=2)
        self.sizeRadioVillage.grid(column=1,row=3)
        self.sizeRadioTown.grid(column=1,row=4)
        self.sizeRadioCity.grid(column=2,row=2)
        self.sizeRadioMetropolis.grid(column=2,row=3)
        self.sizeSlider.grid(column=2,row=4)

    def pressed(self):
        t = Town(popK=self.sizeSelected.get())
        t.output()
        self.adjustReadPoint()

class InnPane(Pane):

    def __init__(self, master, readPoint):
        super(InnPane,self).__init__(master,readPoint,"Generate Tavern Name")

    def pressed(self):
        print innCreator.nameSelector()
        self.adjustReadPoint()


class EventPane(Pane):

    def __init__(self, master, readPoint):
        super(EventPane,self).__init__(master,readPoint,"Generate Event")

    def pressed(self):
        print eventCreator.eventSelector()
        self.adjustReadPoint()