class PreciousStones:
    numberStones = 0 #create variable to count
    stoneCollection = [] # Create list to store in name

    def __init__(self, name):
        self.name = name # Create name object

        if PreciousStones.numberStones <= 5: # If statement while count is less than 5 append list
            PreciousStones.stoneCollection.append(self)# Append list

        else:# Else statemen for when list is over 5
            del PreciousStones.stoneCollection[0]# Delete first index of the list
            PreciousStones.stoneCollection.append(self)# Append list with new name

    @staticmethod
    def displayStones():
        for stones in PreciousStones.stoneCollection:# For loop to print out names
            print(stones.name, end = " ")# Print of list names
    print()

stoneOne = PreciousStones("1")
stoneTwo = PreciousStones("2")
stoneThree = PreciousStones("3")
stoneFour = PreciousStones("4")
stoneFive = PreciousStones("5")
stoneFive.displayStones()
stoneSix = PreciousStones("5")
stoneSix.displayStones()
