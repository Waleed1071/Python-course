menu = ["coffe","latte","capuchino","moka"]

def find_coffie(coffie):
    if coffie[0]  =='c':
        return coffie

filter_coffie = filter(find_coffie , menu)

for x in filter_coffie:
    print(x)