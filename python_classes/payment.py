class payslips():
    def __init__(self , name ,payment , amount) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount 
    def pay(self):
        self.payment = "yes"
    
    def status(self):
        if self.payment == "yes":
            return self.name + " paid "+ str(self.amount)
        else:
            return self.name + " is not paid yet"
        
waleed = payslips("waleed", "no" , 2000)
saeed = payslips("saeed","no",3500)

print(waleed.status() + "\n"+saeed.status())

waleed.pay()
print("\n"+waleed.status() + "\n"+saeed.status())
