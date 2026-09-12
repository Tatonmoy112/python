class Bank:
    total_account=0
    def __init__(self):
        Bank.total_account+=1
        self.account_num= Bank.total_account
        self.balance=0
    
    def deposite(self,amount):
        self.balance+=amount
        print("Successfully debit money in your account.")

    def withdraw(self,amount):
        if self.balance <amount:
            print("In your account doesn't have enough money.So you can't withdraw moeny.Please try again.\nThank You")
        else:
            self.balance-=amount
            print("Successfully credit money from your account.")        

    def show_balance(self):
        print(f"Account number is {self.account_num} : {self.balance}")

    def info(self):
        system=False
        while not system:
            ipt=input("Welcome to TAT Bank.\n"
                      "1.Show Balance\n"
                      "2.Deposite\n"
                      "3.Whitdraw\n"
                      "4.Exit\n"
                      "Choose your service: ")
            if ipt.capitalize()=="Show Balance" or ipt=="1":
                self.show_balance()
            elif ipt=="2" or ipt.capitalize() == "Deposite":
                dep_ammount=int(input("Enter your ammount for deposite: "))
                self.deposite(dep_ammount)
            elif ipt=="3" or ipt.capitalize() == "Withdraw":
                dep_ammount=int(input("Enter your ammount for withdraw: "))
                self.withdraw(dep_ammount)
            elif ipt=="4" or ipt.capitalize() == "Exit":
                print("Thank You visit again.")
                system=True

B=Bank()
B.info()