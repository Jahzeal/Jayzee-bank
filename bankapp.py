import csv
import random as t
import sys
# from csv import reader
# print("welcome to jayzee bank")


class Bank:
    def __init__(self, username, password,createpin2):
        self.username = username
        self.password = password
        self.balance = 0
        self.createpin2 = createpin2
        self.airtime = ["airtel", "mtn", "glo", "9mobile"]
        # self.account_number = account_number

    def create_account(self):
        while True:
            self.Username = input("create user name ")
            self.password = input("create password ")
            if len(self.password) < 8 or ' ' in self.Username or ' ' in self.password:
                print(f"{self.Username} create a valid password of 8 characters excluding white spaces")
                continue
            else:
                print(f'{self.Username} you have created an account')
                self.account_number = t.randint(1000000000, 2000000000)
                self.createpin2 = self.create_pin()
                with open('account.csv', mode='a', newline='') as file:
                    writer = csv.writer(file)
                    if file.tell() == 0:  # Write headers only if file is empty
                        writer.writerow(["username", "password", "pin", "account_number", "balance"])
                    writer.writerow([self.Username, self.password, self.createpin2, self.account_number, self.balance])
                    enter = input("do you wish to login ? ")
                    if enter == "yes":
                        bank.success()
                    else:
                        print("bye")
                        sys.exit()


    def login(self):
            User = input("enter username: ")
            pass1 = input("enter password: ")
            pin = input("Enter pin:")
            with open('account.csv', mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == User and pass1 == row[1] and row[2] ==pin:
                        print(f"{User} you are in: WELCOME")
                        return True
                           
                return "invalid details"

    def check_balance(self):
        with open('account.csv', 'r') as file:
            reader = csv.DictReader(file)
            valid_username = False

            while not valid_username:
                try:
                    name = input("Enter Username: ")
                    for i in reader:
                        if name == i['username']:
                            print(f"{name}, your current balance is {i['balance']}")
                            valid_username = True
                            break  # Exit the for loop since a valid username is found

                    if not valid_username:
                        print("Invalid username! Please try again.")
                        file.seek(0)  # Reset the file position to the beginning for the next iteration
                except ValueError:
                    print("Enter numbers only")





    def create_pin(self):
        while True:
            self.createpin2 = input("create a 4 digits pin of 4 different values",)
            if len(self.createpin2) == 4 and self.createpin2[0] != self.createpin2[1] and self.createpin2[2] != \
                    self.createpin2[3]:
                return self.createpin2

            print(f"{self.createpin2} create a valid pin")
            continue

    def deposit(self):
        with open('account.csv', 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            name = input("Enter Username: ")
            amt = float(input("amount"))
            Found = False
            rows = []
            for i in reader:
                if name == i['username']:
                    i['balance'] = str(float(i['balance']) + amt)
                    Found = True
                rows.append(i)
        if Found:
            with open("account.csv", "w", newline='',encoding="utf-8") as file:
                headers = ['username', 'password', 'pin','account_number','balance']
                csv_write = csv.DictWriter(file, fieldnames=headers)
                csv_write.writeheader()
                csv_write.writerows(rows)
                print(f"{name}.You have successfully made a deposit of {amt}")
        else:
            print(f"Enter your correct Username to deposit {name} not found!.")







    


    def transfer(self):
        while True:
            bank1 = input("Enter account number: ")
            if len(bank1) == 10:
                while True:
                    try:
                        with open('account.csv', mode='r', newline='', encoding='utf-8') as file:
                            reader = csv.DictReader(file)
                            for row in reader:
                                amount1 = float(input("Enter an amount: "))
                                name = input("Enter username")
                                pin1 = input("Enter your pin: ")
                                if amount1 <= float(row["balance"]):
                                    if name == row['username']  and row['pin'] == pin1:  # Access by column name
                                        row['balance'] = str(float(row['balance']) - amount1)
                                        return "Transfer successful!"
                                    else:
                                        return "Invalid pin"
                                else:
                                    return "Insufficient balance"
                    except ValueError:
                        print("Please input numbers only")
            else:
                return 'Invalid account number'



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
                                    return f"{self.username} your current balance is {self.balance}"
                                print(f"{self.username} enter correct pin")

                        print(f"{self.username} input a correct number")

                print(f"{self.username} your balance is not enough")
                continue

            print(f"{self.username} enter a valid network")

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
            pass
        else:
            return "bye"
        try:
            while successfull_login:
                while True:
                    know = int(input("enter 1 to check balance, 2 to transfer, 3 to check balance, and 4 to "
                             "buy airtime and 5 to deposit and 6 end the program "))
                    if know == 1 or know == 2 or know == 3 or know == 4 or know == 5 or know ==6:
                        if know == int(1):
                            return bank.check_balance()
                        elif know == int(2):
                                return bank.transfer()
                        elif know == int(3):
                            return bank.check_balance()
                        elif know == int(4):
                            return bank.buyairtime()
                        elif know == int(5):
                            return bank.deposit()
                        elif know == int(6):
                            return "bye"
                    else:
                        print("enter from range 1 to 5")
         


        except ValueError:
                print("please input numbers only")


bank = Bank("username","password","pin")

    
# print(final())
# bank = Bank("username","password")
# print(success())


# ty = Bank("user_name", "password")
# print(ty.create_account())
# print(ty.login())
# print(ty.account_number())
# print(ty.deposit())
# print(ty.create_pin())
# print(ty.transfer())
# print(ty.buyairtime())
