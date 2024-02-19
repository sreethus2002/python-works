#object

class bank:
    accno:int
    ac_type:str
    balance:int
    bank_name:str="SBI"
    person:str
    ifsc_code:int
    def __init__(self,accno,ac_type,balnce,bank_name,person, ifsc_code):
        self.accno=accno
        self.ac_type=ac_type
        self.balance=balnce
        self.person=person
        self.ifsc_code=ifsc_code
    
    def withdraw(self,amount):
        if self.balance>amount:
            self.balance -=amount
            print(f"your {self.bank_name} account debited with amount {amount} aval bal {self.balance}")
        else:
            print("transaction cancelled.....")


    def deposit(self,amount):
        self.balance+=amount
        print(f"your {self.bank_name} account credited with amount {amount} aval bal {self.balance}")

    def balance_enq(self):
        print(f"your {self.bank_name} accont balance is {self.balance}")


obj1=bank(1234,"savings",200000,"sreethu",12345666)
obj1.balance_enq()
obj1.withdraw(200)
obj1.deposit(300000)


