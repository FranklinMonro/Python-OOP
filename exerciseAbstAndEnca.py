class CarPick: # Create class
    def __init__(self):
        self.carType = {"HATCHBACK": 30,
                        "SEDAN": 50,
                        "SUV":100}

    def displayCar(self):
        print("Pick one of the following cars")
        print("Choice 1 is a Hatchback at cost per day of $",self.carType["HATCHBACK"])
        print("Choice 2 is a Sedan at cost per day of $",self.carType["SEDAN"])
        print("Choice 3 is a SUV at cost per day of $",self.carType["SUV"])

    def calculateCost(self,typeCar, amountDays):
        print()
        print("You have picked the following car: ", typeCar)
        print("You want the car for ", amountDays, " of days")
        print("The cost for renting will be: ", self.carType[typeCar] * amountDays)
        print()






car = CarPick()
choice = ""
while choice != 3:
    print("Choose one of the following")
    print("Choice 1 display choices of cars")
    print("Choice 2 calculate cost to rent car")
    print("Choice 3 exit")
    choice = int(input("Please choose one of the above: "))
    if choice == 1:
        print()
        car.displayCar()
        print()
    elif choice == 2:
        typeCar = input("Please select car: ").upper()
        amountDays = int(input("How many days do you need the car: "))
        car.calculateCost(typeCar,amountDays)
    elif choice == 3:
        break
    else:
        print("You did not make a choice!")
