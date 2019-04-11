class Employee:
    def setNumberOfWorkingHours(self):
        self.numberOfWorkingHOurs = 48

    def displayNumberOfWorkingHours(self):
        print(self.numberOfWorkingHOurs)

class Trainee(Employee):
    def setNumberOfWorkingHours(self):
        self.numberOfWorkingHOurs = 45

    def resetNumberOfWorkingHours(self):
        super().setNumberOfWorkingHours()

employee = Employee()
employee.setNumberOfWorkingHours()
print("Number of working hour fo employee: ", end = " ")
employee.displayNumberOfWorkingHours()
trainee = Trainee()
trainee.setNumberOfWorkingHours()
print("Number of working hour fo trainee: ", end = " ")
trainee.displayNumberOfWorkingHours()
trainee.resetNumberOfWorkingHours()
print("Number of working hour fo trainee after reset: ", end = " ")
trainee.displayNumberOfWorkingHours()
