def test(a,b):
    return a/b

try:
    ans=test(40,0)
except Exception as e:
    print("somthing wrong ",e)
    print(e.__class__)