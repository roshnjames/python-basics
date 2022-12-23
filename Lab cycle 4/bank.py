class bank:
    def __init__(self,name,no,acctype,bal):
        self.name=name
        self.no=no
        self.acctype=acctype
        self.bal=bal
    def deposit(self):
        nbal=float(input("Enter the deposit amount"))
        self.bal=self.bal+nbal
        print("current balance is ",self.bal)
    def withdraw(self):
        wbal=float(input("Enter the withdrawal amount"))
        if wbal>self.bal:
            print("Not enough balance")
        else:
            self.bal=self.bal-wbal
            print("current balance is ",self.bal)



name=input("Enter name of the user")
no=int(input("Enter account number"))
acctype=input("Enter the type of bank account")
bal=int(input("Enter current balance"))

bnk1=bank(name,no,acctype,bal)
n=0
while(n!=3):
    n=int(input("ENter your operation\n1. deposit\n2.withdraw\n3.exit\n"))
    if(n==1):
        bnk1.deposit()
    elif(n==2):
        bnk1.withdraw()
    elif(n==3):
        print("Exiting")
    else:
        print("Enter valid choice!")
