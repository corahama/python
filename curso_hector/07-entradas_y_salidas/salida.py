v = "otro texto"
n = 10

print("un texto", v, "y un numero", n)

c = "un texto '{1}' y un numero '{0}'".format(v, n)
print(c)

c = "un texto '{t}' y un numero '{n}'".format(t = v, n = n)
print(c)

c = "{v}, {v}, {v}".format(v=v)
print(c)

print("{:>30}".format("palabra"))
print("{:30}".format("palabra"))
print("{:^30}".format("palabra"))
print("{:.3}".format("palabra"))
print("{:>30.3}".format("palabra"))

print("{:4d}".format(10))
print("{:4d}".format(100))
print("{:4d}".format(1000))

print("{:04d}".format(10))
print("{:04d}".format(100))
print("{:04d}".format(1000))

print("{:07.2f}".format(3.1415926))
print("{:07.2f}".format(512.21))
