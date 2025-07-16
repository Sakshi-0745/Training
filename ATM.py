class atm:
    def __init__(self,balance,pin,deposite,withdraw):
        self.balance = balance
        self.pin = ""
        self.deposite = deposite 
        self.withdraw = withdraw
    def show_menu(self):
        print("1. Check menu")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
    
    def create_pin(self):
        create_pin = int(input("Create pin"))
        confirm_pin = input("Confirm Pin")
        if create_pin == confirm_pin:
            print("Pin created successfully")
        else:
            print("Pin did not match")
            self.create_pin()
    def pin(self):
        user_pin = input("Enter your pin:")
        self.pin = user_pin
        create_pin = input("Create a pin:")
        if user_pin == create_pin:
            print("Pin created successfully")
        else:
            print("Pin does not match, please try again")
            self.pin()
    def balance(self):
        self.balance = 0
        print("Your balance is",self.balance)
    def deposite(self):
        Amount = int(input("Enter a amount to deposite"))
        self.balance =+ Amount
        print("New Balance is:",self.balance)
    def withdraw(self):
        Amount = int(input("Enterr a amount to withdraw"))
        if Amount >self.balance:
            print("Insufficient Balance")
        else:
            print("Withdraw amount is:, Amount")
            self.withdraw = Amount
            self.balance =- Amount
        print("New balance is:",self.balance)           
