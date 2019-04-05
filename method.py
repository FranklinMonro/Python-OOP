class Employee:
    def employeeDetails(self):
        self.name = "Ben"
        print("Name: ", self.name)

    @staticmethod
    def welcomMessage():
        print("Welcome to our organization")

employee = Employee()
employee.employeeDetails()
employee.welcomMessage()
