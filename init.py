class Employee:
    def __init__(self,name):
        self.name = name


    def displayEmployeeDetails(self):
        print(self.name)


employeeOne = Employee("mark")
employeeTwo = Employee("matthew")
employeeOne.displayEmployeeDetails()
employeeTwo.displayEmployeeDetails()
