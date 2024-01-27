class Employees:
    def __init__(self , name , last) -> None:
        self.name = name
        self.last = last

class Supervisior(Employees):
    def __init__(self, name, last , password) -> None:
        super().__init__(name, last)
        self.password = password

class chef(Employees):
    def leave_req(self,days):
        return "May i take a leave for "+str(days)+ " days"


waleed = Supervisior("waleed","W", "Apple")
abeed = chef("Abeed", "A")
saad = chef("saad","S")

print(saad.leave_req(3))
print(waleed.password)
print(abeed.name)
    