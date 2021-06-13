# PARTE UNO
import re

texto = "En esta cadena se encuentra una palabra mágica"
encontrado = re.search('mágica', texto)
print(encontrado.span())
print(encontrado.string)

texto = "Hola mundo"
encontrado =  re.match('Hola', texto)

texto = "Vamos a dividir esta cadena"
palabras = re.split(' ', texto)
print(palabras)

texto = "Hola amigo"
print(re.sub("amigo", "amiga", texto))

texto = "hola adios hola hola"
print(re.findall("hola", texto))

texto = "hola adios hello hola bye"
print(re.findall("hola|hello", texto))


# PARTE DOS
print("\nParte dos")
texto = "hla hola hoola hooola hoooola"

def buscar(patrones, texto):
    for patron in patrones:
        print( re.findall(patron, texto))

patrones = ['hla', 'hola', 'hoola']
buscar(patrones, texto)

print("")
patrones = ['ho', 'ho*', 'ho*la']
buscar(patrones, texto)

print("")
patrones = ['ho*', 'ho+', 'ho?', 'ho?la']
buscar(patrones, texto)

print("")
patrones = ['ho{0}la', 'ho{1}la', 'ho{2}la']
buscar(patrones, texto)

print("")
patrones = ['ho{0,1}la', 'ho{1,2}la', 'ho{2,10}la']
buscar(patrones, texto)


# PARTE TRES
print("\nParte tres")
texto = 'hala hela hila hola hula'
print("")
patrones = ['h[au]la']
buscar(patrones, texto)

texto = 'haaaala heeeeela hoola huuuuuuuuuula'
print("")
patrones = ['h[au]*', 'h[eo]*la', 'h[oe]{2,9}la']
buscar(patrones, texto)

texto = 'hala hela hila hola hula'
print("")
patrones = ['h[^o]la']
buscar(patrones, texto)

texto = 'hola h0la Hola mola m0la M0la sdha asAs U234 Yads'
print("")
patrones = ['h[a-z]la', 'h[0-9]la', '[A-z]{4}', '[A-Z][a-z0-9]{3}']
buscar(patrones, texto)

texto = 'Este curso de python 3 fue publicado en el año 2016'
print("")
patrones = [r'\d', r'\d+', r'\D', r'\D+', r'\s', r'\S', r'\S+', r'\w', r'\w+', r'\W', r'\W+', ]
buscar(patrones, texto)
