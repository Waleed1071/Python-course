class recipe():
    def __init__(self , dish , item , time) -> None:
        self.dish = dish
        self.item = item
        self.time = time

    def contents(self):
        print("The "+ self.dish + " has "+ str(self.item) + " and takes " +\
              str(self.time) + " min to prepare ")
        

pizaa = recipe("Pizza" , ["chesse","bread","sauce"],45)
paste = recipe("pasta", ["pasta","chicken","sauce"], 55)

print(pizaa.item)
print(pizaa.contents())