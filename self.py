class Employee:
    def employeeDetails(self):
        self.name = "Matthew"
        print("Name is: ", self.name)
        age = 30
        print("Age is: ", age)

    def printEmployeeDetails(self):
        print("Printing from another method")
        print("Name: ", self.name)
        print("Age ", age)

employee = Employee()
employee.employeeDetails()
employee.printEmployeeDetails()
