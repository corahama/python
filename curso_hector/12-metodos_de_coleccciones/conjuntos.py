c = set()
c.add(1)
c.add(2)
c.add(3)
print(c)

c.discard(1)
print(c)
c.add(1)
print(c)

c.add(4)
c2 = c.copy()
c2.discard(4)
print(c)
c2.clear()
print(c2)

c1 = {1,2,3}
c2 = {3,4,5}
c3 = {-1,99}
c4 = {1,2,3,4,5}
print(c1.isdisjoint(c3))
print(c1.issubset(c4))
print(c4.issuperset(c1))
print(c1.union(c2))
c1.update(c2)
print(c1)
print(c1.difference(c2))
c1.difference_update(c2)
print(c1)

c1 = {1,2,3}
c2 = {3,4,5}
c3 = {-1,99}
c4 = {1,2,3,4,5}
print(c1.intersection(c2))
print(c1.symmetric_difference(c2))
