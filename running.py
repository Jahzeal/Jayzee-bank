from bankapp import Bank


def final():
    print("welcome to Jayzee bank")
    confirmTrue = bank.confirm()
    if confirmTrue:
        check_ussd = input("enter ussd ")
        if check_ussd == "*904#":
            bank.create_account()
            bank.success()
        else:
             print("invalid")
    else:
         bank.success()
        
        
    
bank = Bank("username","password")
print(final())           
