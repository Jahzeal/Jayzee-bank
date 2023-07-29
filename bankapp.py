import csv
import random as t

# print("welcome to jayzee bank")


class Bank:
    def __init__(self, username, password):
        self.Username = username
        self.password = password
        self.balance = 0
        self.createpin2 = ""
        self.airtime = ["airtel", "mtn", "glo", "9mobile"]
    def create_account(self):
        while True:
            self.Username = input("create user name ")
            self.password = input("create password ")
            if len(self.password) < 8 or ' ' in self.Username or ' ' in self.password:
                print(f"{self.Username} create a valid password of 8 characters excluding white spaces")
                continue
            else:
                print(f'{self.Username} you have created an account')
                with open('account.csv', mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([self.Username, self.password])

                return

    def account_number(self):
        num1 = t.randint(1000000000, 2000000000)
        return f"{self.Username} here is your account number {num1}"

    def login(self):
        enter = input("do you wish to login ? ")
        if enter == "yes":
            while True:
                User = input("enter username")
                pass1 = input("enter password")
                with open('account.csv', mode='r') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        if User == row[0] and pass1 == row[1]:
                            return (f"{User} you are in")
                        else:
                            return"invalid details"
        else:
            return False

    def check_balance(self):
        return f"{self.Username} here is your account balance {self.balance}"

    def create_pin(self):
        while True:
            self.createpin2 = input("create a 4 digits pin of 4 different values",)
            if len(self.createpin2) == 4 and self.createpin2[0] != self.createpin2[1] and self.createpin2[2] != \
                    self.createpin2[3]:
                print( "here is your pin")
                return

            print(f"{self.createpin2} create a valid pin")
            continue

    def deposit(self):
        while True:
            amount = int(input("enter an amount to deposit, you have to deposit to perform other functions "))
            if int(amount) > 0:
                self.balance += amount
                return f"{self.Username} you have succefully deposited {amount}"
            else:
                print(f"{self.Username} you cant deposit zero naira")

    def transfer(self):
        while True:
            bank1 = input("enter account number")
            if len(bank1) == 10:
                while True:
                    try:
                        amount1 = int(input("enter an amount"))
                        if amount1 <= self.balance:
                            pin1 = input("enter your pin")
                            if pin1 == self.createpin2:
                                self.balance -= amount1
                                return "success"
                            else:
                                return 'invalid pin'
                        else:
                            return "insuficient balance"
                    except ValueError:
                        print("please input numbers only")
            else:
                return 'invalid account number'

    def buyairtime(self):
        while True:
            buy1 = input("what network do you want")
            if buy1 in self.airtime:
                amount_air = int(input("amount"))
                if amount_air <= self.balance:
                    while True:
                        num1 = input("enter a number")
                        if len(num1) == 11:
                            while True:
                                check_pin = input("enter pin")
                                if check_pin == self.createpin2:
                                    self.balance -= amount_air
                                    print("success")
                                    return f"{self.Username} your current balance is {self.balance}"
                                print(f"{self.Username} enter correct pin")

                        print(f"{self.Username} input a correct number")

                print(f"{self.Username} your balance is not enough")
                continue

            print(f"{self.Username} enter a valid network")

            continue

    def confirm(self):
        try:
            print("Enter 1 to login and 2 to create account")
            confirm1 = int(input("!"))
            if confirm1 == 2:
                return True
            
            elif confirm1 == 1:
                return False
        except ValueError:
            print("please input numbers only")
    

    def success(self):
        successfull_login = bank.login()
        if successfull_login:
            bank.create_pin()
        else:
            return "bye"
        try:
            while successfull_login:
                yu = bank.account_number()
                print(yu)
                yl = bank.deposit()
                print(yl)
                while True:
                    know = int(input("enter 1 to check balance, 2 to transfer, 3 to check balance, and 4 to "
                             "buy airtime"))
                    if know == 1 or know == 2 or know == 3 or know == 4:
                        if know == int(1):
                            gw = bank.check_balance()
                            print(gw)
                        elif know == int(2):
                                io = bank.transfer()
                                print(io)
                        elif know == int(3):
                            ju = bank.check_balance()
                            print(ju)
                        elif know == int(4):
                            so = bank.buyairtime()
                            print(so)
                    else:
                        print("enter from range 1 to 4")
         


        except ValueError:
                print("please input numbers only")


bank = Bank("username","password")