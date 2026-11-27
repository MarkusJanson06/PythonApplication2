import math     #ilma from-ita
print("Ruudu karakteristikud")
a=float(input('Sisesta ruudu külje pikkus => '))   #lisasin float
S=a**2
print("Ruudu pindala", S)
P=4*a
print("Ruudu ümbermõõt", P)   # jutumätgid ühesugused
di=a*math.sqrt(2)   # mitte sqr vaid sqrt
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud")    # liigne sulg
b=float(input("Sisesta ristküliku 1. külje pikkus => "))  # lisasin float
c=float(input("Sisesta ristküliku 2. külje pikkus => "))  # lisasin float
S=b*c
print("Ristküliku pindala", S)   #lisasin jutumärgi algusesse
P=2*(b+c)    # lisasin *
print("Ristküliku ümbermõõt", P)
di=math.sqrt(b**2+c**2)  # kaks *
print("Ristküliku diagonaal", round(di, 2))    # üks puuduv sulg; mitte round(di) vaid round(di,2)
print()
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiuse pikkus => "))  # liigne sulg; lisasin float
d=2*r  # lisasin *
print("Ringi läbimõõt", d)  # puudus ,
S=math.pi*r**2   #kaks * ja  math.pi
print("Ringi pindala", round(S))
C=2*math.pi*r
print("Ringjoone pikkus", round(C, 2))     # puuduv sulg
