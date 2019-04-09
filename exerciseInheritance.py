class Furniture:    # Base class
    _typeOfWood = "Teakwood" # Protected property

class Chair(Furniture): # Inheritance class
    def __init__(self):
        self.__numberOfLegs = 4 # Private property

    def changeWood(self,change):    # Function to change the wood
        self._typeOfWood = change
        print("The chair will be made of {} and will have {} legs".format(self._typeOfWood,self.__numberOfLegs))

    def standardWood(self): # Function for just standard wood
        print("The chair will be made of {} and will have {} legs".format(self._typeOfWood,self.__numberOfLegs))



chair = Chair() # Creating of object
choice = input("Do you want to change the wood(Y/N): ").upper() # user input
if choice == 'Y': # Else if statement to change wood
    change = input("What wood do you want to change to: ")
    chair.changeWood(change)
else:
    chair.standardWood()
