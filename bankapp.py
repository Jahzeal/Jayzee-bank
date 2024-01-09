import csv
import random as t
import sys



class Bank:
    def __init__(self, username, password,createpin2):
        self.username = username
        self.password = password
        self.balance = 0
        self.createpin2 = createpin2
        self.airtime = ["airtel", "mtn", "glo", "9mobile"]

    def create_account(self):
        while True:
            self.Username = input("create user name ")
            self.password = input("create password ")
            if len(self.password) < 8 or ' ' in self.Username or ' ' in self.password:
                print(f"{self.Username} create a valid password of 8 characters excluding white spaces")
                continue
            else:
                print(f'{self.Username} you have created an account: ')
                self.account_number = t.randint(1000000000, 2000000000)
                self.createpin2 = self.create_pin()
                with open('account.csv', mode='a', newline='',encoding='utf-8') as file:
                    writer = csv.writer(file)
                    if file.tell() == 0:  # Write headers only if file is empty
                        writer.writerow(["username", "password", "pin", "account_number", "balance"])
                    writer.writerow([self.Username, self.password, self.createpin2, self.account_number, self.balance])
                    print("Account succesfully created")
                    sys.exit()


    def login(self):
            User = input("enter username: ")
            pass1 = input("enter password: ")
            pin = input("Enter pin:")
            with open('account.csv', mode='r',encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == User and pass1 == row[1] and row[2] ==pin:
                        print(f"{User} you are in: WELCOME")
                        return True
                           
                print("invalid details")
                return False

    def check_balance(self):
        with open('account.csv', 'r',encoding='utf-8') as file:
            reader = csv.DictReader(file)
            valid_username = False

            while not valid_username:
                try:
                    pin = input("Enter Pin: ")
                    for i in reader:
                        if pin == i['pin']:
                            print(f"{i['username']} your current balance is {i['balance']}")
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
            pin = input("Enter Pin: ")
            amt = float(input("amount"))
            Found = False
            rows = []
            for i in reader:
                if pin == i['pin']:
                    i['balance'] = str(float(i['balance']) + amt)
                    Found = True
                rows.append(i)
        if Found:
            with open("account.csv", "w", newline='',encoding="utf-8") as file:
                headers = ['username', 'password', 'pin','account_number','balance']
                csv_write = csv.DictWriter(file, fieldnames=headers)
                csv_write.writeheader()
                csv_write.writerows(rows)
                print(f"You have successfully made a deposit of {amt}")
                sys.exit()
        else:
            print(f"Enter your correct Username to deposit {self.username} not found!.")


    def transfer(self):
        while True:
            bank1 = input("Enter account number: ")
            if len(bank1) == 10:
                while True:
                    try:
                        with open('account.csv', mode='r', newline='', encoding='utf-8') as file:
                            reader = csv.DictReader(file)
                            rows = list(reader)
                            for row in rows:
                                amount1 = float(input("Enter an amount: "))
                                name = input("Enter username: ")
                                pin1 = input("Enter your pin: ")
                                if amount1 <= float(row["balance"]):
                                    if name == row['username'] and row['pin'] == pin1:
                                        row['balance'] = str(float(row['balance']) - amount1)
                                        print(f"{row['username']}, Transfer successful!")
                                        with open("account.csv", 'w', newline='', encoding='utf-8') as file:
                                            headers = ['username', 'password', 'pin', 'account_number', 'balance']
                                            csv_write = csv.DictWriter(file, fieldnames=headers)
                                            csv_write.writeheader()
                                            csv_write.writerows(rows)
                                        sys.exit()
                                    else:
                                        print("Invalid pin")
                                else:
                                    print("Insufficient balance")
                    except ValueError:
                        print("Please input numbers only")
            else:
                print('Invalid account number')



    def buy_airtime(self):
        while True:
            network_choice = input("What network do you want: ")
            if network_choice.lower() in self.airtime:
                try:
                    amount_air = float(input("Enter the airtime amount: "))
                except ValueError:
                    print("Please enter a valid numeric amount.")
                    continue

                with open('account.csv', 'r', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    rows = list(reader)

                for row in rows:
                    if amount_air <= float(row["balance"]):
                        while True:
                            phone_number = input("Enter the phone number: ")
                            if len(phone_number) == 11:
                                while True:
                                    check_pin = input("Enter your PIN: ")
                                    if check_pin == row["pin"]:
                                        row["balance"] = str(float(row["balance"]) - amount_air)
                                        print("Success! Airtime purchased.")
                                        print(f"{row['username']}, your current balance is {row['balance']}")
                                        with open('account.csv', 'w', newline='', encoding='utf-8') as file:
                                            headers = ['username', 'password', 'pin', 'account_number', 'balance']
                                            csv_write = csv.DictWriter(file, fieldnames=headers)
                                            csv_write.writeheader()
                                            csv_write.writerows(rows)
                                        sys.exit()
                                    print("Invalid PIN. Please try again.")
                            print("Invalid phone number. Please enter a valid 11-digit phone number.")
                        break
                else:
                    print("Insufficient balance!")
            else:
                print("Enter a valid network.")

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
                            return bank.buy_airtime()
                        elif know == int(5):
                            return bank.deposit()
                        elif know == int(6):
                            return "bye"
                    else:
                        print("enter from range 1 to 5")
         


        except ValueError:
                print("please input numbers only")


bank = Bank("username","password","pin")