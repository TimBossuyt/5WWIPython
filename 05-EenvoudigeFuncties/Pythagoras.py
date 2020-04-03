from math import sqrt

a = float(input('Lengte zijde a '))
b = float(input('Lengte zijde b '))

#berekening

c = sqrt(pow(a, 2) + pow(b, 2))

uitvoer = 'In een rechthoekige driehoek met rechthoekszijden a = {:.2f} en b = {:.2f} is de schuine zijde {:.2f}'

print(uitvoer.format(a, b, c))
