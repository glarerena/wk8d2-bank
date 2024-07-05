class BankAccount:
    def __init__(self, accountNumber, accountHolder, initialBalance):
        self.__accountNumber = accountNumber
        self.__accountHolder = accountHolder
        self.__balance = initialBalance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrew {amount}. New balance is {self.__balance}.")
            else:
                print("Error: Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def getBalance(self):
        return self.__balance

    def displayAccountInfo(self):
        print(f"Account Number: {self.__accountNumber}")
        print(f"Account Holder: {self.__accountHolder}")
        print(f"Current Balance: {self.__balance}")

# Main Program to Demonstrate Usage

def main():

    account1 = BankAccount("001", "James G", 1000.0)
    account2 = BankAccount("002", "Rena", 500.0)
    account3 = BankAccount("003", "James W", 200.0)

    # Display account information
    account1.displayAccountInfo()
    account2.displayAccountInfo()
    account3.displayAccountInfo()

    
    # Perform transactions on account1
    account1.deposit(200)
    account1.withdraw(50)

    # Display updated account information for account1
    account1.displayAccountInfo()
    

if __name__ == "__main__":
    main()
