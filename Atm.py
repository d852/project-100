class Atm:
    def __init__(self,cardNumber,pin , balance):
        self.cardNUmber = cardNumber
        self.pin = pin
        self.balance = balance


    def balanceEnquiry(self):
        print("Your blance is " , self.balance)


    def cashWithdrawl(self , amount):
        self.balance = self.balance - amount
        print("your remaining balance is" , self.balance)
        

cardNumber = int(input("Enter your card number: "))
pin = int(input("Enter your pin: "))
balance = int(input("Enter your balance left: "))
atm =  Atm(cardNumber,pin,balance)
choice = int(input("press 1 for withdrawl 2 for balance enquiry: "))

if(choice == 1):
    amount = int(input("Enter the amount you want to wiwthdrawl: "))
    atm.cashWithdrawl(amount)
elif(choice == 2):
    atm.balanceEnquiry()
else:
    print("Enter a valid choice between 1 and 2")

