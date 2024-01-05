import csv
import random as t

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
                    break

    def login(self):
        enter = input("do you wish to login ? ")
        if enter == "yes":
                User = input("enter username: ")
                pass1 = input("enter password: ")
                pin = input("Enter pin:")
                with open('account.csv', mode='r') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        if row[0] == User and pass1 == row[1] and row[2] ==pin:
                            print(f"{User} you are in: WELCOME")
                            return True
                           
                    print("invalid details")
                            
        else:                
            print("bye")
            return False

    def check_balance(self):
        return f"{self.username} here is your account balance {self.balance}"

    def create_pin(self):
        while True:
            self.createpin2 = input("create a 4 digits pin of 4 different values",)
            if len(self.createpin2) == 4 and self.createpin2[0] != self.createpin2[1] and self.createpin2[2] != \
                    self.createpin2[3]:
                return self.createpin2

            print(f"{self.createpin2} create a valid pin")
            continue

    def deposit(self):
        while True:
            try:
                amount = int(input("How much would you like to deposit? "))
                if amount > 0:
                    self.balance += amount  # Update balance in memory

                # Update balance in CSV file (assuming a header row exists)
                    with open('account.csv', mode='r', newline='', encoding='utf-8') as file:
                        reader = csv.reader(file)
                        headers = next(reader)  # Skip the header row
                        data = list(reader)
                    for row in data:
                        if row[0] == self.username:
                            row[headers.index("balance")] = str(self.balance)  # Update balance using header index
                            break

                    with open('account.csv', mode='w', newline='', encoding='utf-8') as file:
                        writer = csv.writer(file)
                        writer.writerow(headers)  # Write the header row back
                        writer.writerows(data)  # Write updated data rows

                    print("Deposit successful. Your new balance is:", self.balance)
                    break
                else:
                    print("Invalid amount. Please enter a positive amount.")
            except ValueError:
                print("Invalid input. Please enter a numerical amount.")





    


    def transfer(self):
        while True:
            bank1 = input("Enter account number: ")
            if len(bank1) == 10:
                while True:
                    try:
                        amount1 = int(input("Enter an amount: "))
                        if amount1 <= self.balance:
                            pin1 = input("Enter your pin: ")

                            # Read the CSV file using DictReader
                            with open('account.csv', mode='r', newline='', encoding='utf-8') as file:
                                reader = csv.DictReader(file)
                                for row in reader:
                                    if row['username'] == self.username:  # Access by column name
                                        if row['pin'] == pin1:
                                            self.balance -= amount1
                                            # TODO: Implement logic to transfer funds to the recipient account
                                            return "Transfer successful!"
                                        else:
                                            return "Invaliyyd pin"
                                        break
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
                bank.deposit()
                while True:
                    know = int(input("enter 1 to check balance, 2 to transfer, 3 to check balance, and 4 to "
                             "buy airtime and 5 to end the program "))
                    if know == 1 or know == 2 or know == 3 or know == 4 or know == 5:
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
                        elif know == int(5):
                            return "bye"
                    else:
                        print("enter from range 1 to 5")
         


        except ValueError:
                print("please input numbers only")


bank = Bank("username","password","oin")

    
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
