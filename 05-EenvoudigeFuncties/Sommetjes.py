a = int(input('Geef het eerste getal tussen 0 en 20? '))
b = int(input('Geef het tweede getal tussen 0 en 20? '))

#berekening


#uitvoer
uitvoer = '{:>6d} + {:<6d} = {:<6d}'

i = 0
print(uitvoer.format(a*pow(10, i), b*pow(10, i), a*pow(10, i)+ b*pow(10, i)))
i += 1

print(uitvoer.format(a*pow(10, i), b*pow(10, i), a*pow(10, i)+ b*pow(10, i)))
i += 1

print(uitvoer.format(a*pow(10, i), b*pow(10, i), a*pow(10, i)+ b*pow(10, i)))
i += 1

print(uitvoer.format(a*pow(10, i), b*pow(10, i), a*pow(10, i)+ b*pow(10, i)))
i += 1

print(uitvoer.format(a*pow(10, i), b*pow(10, i), a*pow(10, i)+ b*pow(10, i)))
