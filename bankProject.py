from abc import ABCMeta, abstractmethod
import random
class BankAccount(metaclass = ABCMeta):
    @abstractmethod
    def addAccount():
        return 0
    @abstractmethod
    def authenticate():
        return 0
    @abstractmethod
    def depositFunds():
        return 0
    @abstractmethod
    def withdrawFunds():
        return 0
    @abstractmethod
    def displayBalance():
        return 0

class SavingAccounts:
    def __init__(self):
        self.accounts = {}


    def addAccount(self, customerName, customerDeposit):  # Method to add a account
        self.customerAccNumber = random.randint(10000,99999) # Create random 5 digit number
        self.accounts[self.customerAccNumber] = [customerName,customerDeposit] # Create a dictionary entry, as yor account number as key
        print("Your account number is: ", self.customerAccNumber) # Print out the account number

    def authenticate(self, customerName, customerAccNumber): # Method to authenticate if the user exist
        if customerAccNumber in self.accounts.keys(): # If statement to check if the account number exist as key in dictionary
            if self.accounts[self.customerAccNumber][0] == customerName: # If statement to check if name exist in the given key
                print("Authenticated Successfull")
                self.customerAccNumber = customerAccNumber
                return True
            else:
                print("Authenticated Failed")
                return False
        else:
            print("Authenticated Failed")
            return False

    def depositFunds(self,depositAmmount): # Method to deposit funds
        self.accounts[self.customerAccNumber][1] += depositAmmount # Add the funds to existing amount
        self.displayBalance() # Calls the display method

    def withdrawFunds(self,withDrawAmmount): # Method to witdraw funds
        if withDrawAmmount > self.accounts[self.customerAccNumber][1]: # If statement to check if amount to withdraw is less or more than amount in funds
            print("Insufficient Balance")
        else:
            self.accounts[self.customerAccNumber][1] -= withDrawAmmount # Minus the amount from the funds
            print("Withdrawal was Successfull")
            self.displayBalance() # Calls the display method


    def displayBalance(self): # Method to display amount in account
        print("Available balance: ", self.accounts[self.customerAccNumber][1])


customer = SavingAccounts()

choice = ""
selectOption = ""
while choice != "N":
    choice = input("Do you need assistance(Y/N)").upper()
    if choice == "Y":
        print("Please choose what you need to do?")
        print("1. Open a account\n"
              "2. Existing account\n"
              "3. Exit")
        select = int(input("Please select option: "))

        if select == 1:
            customerName = input("Please enter your name: ")
            customerDeposit = int(input("Please enter your deposit: "))
            customer.addAccount(customerName, customerDeposit)
        elif select == 2:
            customerName = input("Please enter your name: ")
            customerAccNumber = int(input("Please enter your Account Number: "))
            authStatus = customer.authenticate(customerName,customerAccNumber)
            if authStatus == True:
                while selectOption != 4:
                    print("1. Deposit Funds\n"
                          "2. Withdraw Funds\n"
                          "3. Account Balance\n"
                          "4. Go back to previos menu")
                    selectOption = int(input("Please enter your selection: "))
                    if selectOption == 1:
                        depositAmmount = int(input("How much do you want to deposit: "))
                        customer.depositFunds(depositAmmount)
                    elif selectOption == 2:
                        withDrawAmmount = int(input("How much dou you want to withdraw?: "))
                        customer.withdrawFunds(withDrawAmmount)
                    elif selectOption == 3:
                        customer.displayBalance()
                    elif selectOption == 4:
                        break
        elif select == 3:
            break
        else:
            print("Incorrect selection")
