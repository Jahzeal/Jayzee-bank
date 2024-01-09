from bankapp import Bank


def final():
    print("welcome to Jayzee bank")
    confirmTrue = bank.confirm()
    if confirmTrue:
        while True:
            check_ussd = input("enter ussd ")
            if check_ussd != "*904#":
                print("invalid")
            else:
                bank.create_account()
                return bank.success()
                
    else:
         return  bank.success()
        
        
    
bank = Bank("username","password","pin")
(final())