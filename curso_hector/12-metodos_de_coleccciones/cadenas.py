print("Hola mundo".upper())
print("Hola mundo".lower())
print("hola mundo".capitalize())
print("hola mundo".title())
print("hola mundo".count('o'))
print("hola mundo".count('mundo'))
print("hola mundo".find('mundo'))
print("hola mundo mundo mundo".rfind('mundo'))

c = "100"
print(c.isdigit())
c2 = "ABC1234po"
print(c.isalnum()) #Alfanumerico
c3 = "ABC"
print(c3.isalpha())

h = "Hola mundo"
print(h.isupper())
print(h.islower())
print(h.istitle())

print("    ".isspace())

print(h.startswith("Hola"))
print(h.endswith('o'))

print("Hola mundo mundo".split())
print("Hola,mundo,mundo,otra,palabra".split(','))

print(",".join("Hola mundo"))
print(" ".join("Hola mundo"))

print("-----hola-----".strip('-'))

print("Hola mundo".replace('mundo','marte'))

print("Hola mundo mundo mundo mundo mundo".replace(" mundo", '', 4))
