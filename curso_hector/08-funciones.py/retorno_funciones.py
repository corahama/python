def test():
    return [0,1,2,3,4]

print(test()[1:4])
print(test()[-1])

def test1():
    return "una cadena",5,[1,2,3]

print(test1())

c,n,l = test1()
print(c)
print(n)
print(l)
