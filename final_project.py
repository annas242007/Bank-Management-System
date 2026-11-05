
# BANK SYSTEM - OOP FINAL PROJECT.
from abc import ABC, abstractmethod

class Bank(ABC):

    def __init__(self, acc_no, name, balance=0):
        self.acc_no = acc_no          
        self.name = name              
        self.__balance = balance
        self.history = []

    def get_balance(self):
        return self.__balance        

    def set_balance(self, amount):
        self.__balance = amount      

    def check_balance(self):
        print("Account No:", self.acc_no)
        print(" Name:", self.name)
        print("The balance in your account is: ", self.__balance)

    def show_history(self):
        print("Transaction History of", self.name)
        if len(self.history) == 0:    
            print("No transactions yet")  
        else:
            for item in self.history:    
                print("-", item)            

    
    
    def deposit(self, amount):
        if amount <= 0:              
            print("Please deposit some amount")
        else:
            self.__balance += amount  
            self.history.append("Deposit: " + str(amount))
            print("Amount successfully deposited")


   
    @abstractmethod
    def withdraw(self, amount):
        pass                          

class SavingsAccount(Bank):

    def withdraw(self, amount):
        
        if amount<=0:
            print("Amount cannot be negative")
            return False
            
        elif self.get_balance() >= amount:
            self.set_balance(self.get_balance() - amount)
            self.history.append("Withdraw: " + str(amount))
            print("Withdraw successful")
            return True              
        else:
            print("Insufficient Balance")
            return False             

class CurrentAccount(Bank):

    def withdraw(self, amount):
        
        if amount<=0:
            print("Amount cannot be negative")
            return False
        
        
        elif self.get_balance() + 5000 >= amount:
            self.set_balance(self.get_balance() - amount)
            self.history.append("Withdraw: " + str(amount))
            print("Withdraw successful")
            return True
        else:
            print("Overdraft limit exceeded")
            return False




accounts = {}


next_no = 1001



def find_account(acc_no):
    if acc_no in accounts:            
        return accounts[acc_no]      
    print("Account not found")      
    return None                       


while True:

    print("\nMenu")
    print("1. Create Account")
    print("2. Check Balance")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Transfer")
    print("6. Transaction History")
    print("7. Exit")

    
    try:
        
        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter account holder name: ")      
            type = int(input("1. Savings  2. Current : "))   
                   

            if type == 1:
                opening = int(input("Opening balance: ")) 
                accounts[next_no] = SavingsAccount(next_no, name, opening)
                
            elif type==2:
                opening = int(input("Opening balance: ")) 
                accounts[next_no] = CurrentAccount(next_no, name, opening)
            
            else:
                print("Invalid type")
                continue

            print("Account created! Your account number is:", next_no)
            next_no += 1   

        elif choice == 2:
            acc = find_account(int(input("Enter account number: ")))
            if acc is not None:      
                acc.check_balance()

        elif choice == 3:
            acc = find_account(int(input("Enter account number: ")))
            if acc is not None:
                amount = int(input("Enter amount you want to deposit : "))
                acc.deposit(amount)

        elif choice == 4:
            acc = find_account(int(input("Enter account number: ")))
            if acc is not None:
                amount = int(input("Enter amount you want to withdraw : "))
                acc.withdraw(amount)

        elif choice == 5:
            from_no = int(input("Enter YOUR account number: "))
            to_no = int(input("Enter RECEIVER account number: "))
            sender = find_account(from_no)      
            receiver = find_account(to_no)      

            if sender is not None and receiver is not None:
                if from_no == to_no:
                    print("Apne aap ko transfer nahi kar sakte")
                else:
                    amount = int(input("Enter amount to transfer : "))
                    if amount <= 0:
                        print("Amount 0 se zyada hona chahiye")
                    elif sender.withdraw(amount):
                        receiver.deposit(amount)
                        print("Transfer successful")

        elif choice == 6:
            acc = find_account(int(input("Enter account number: ")))
            if acc is not None:
                acc.show_history()

        elif choice == 7:
            print("Thank you")
            break           

        else:
            print("Invalid choice")

    except ValueError:
        print("Please enter numbers only")