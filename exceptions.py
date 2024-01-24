def test(a,b):
    return a/b

try:
    ans=test(40,0)
except Exception as e:
    print("somthing wrong")
    print(e)
    print(e.__class__)