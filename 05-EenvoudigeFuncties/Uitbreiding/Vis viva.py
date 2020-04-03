from math import pi, sqrt

r = float(input('Geef de afstand tussen de satelliet en het middelpunt van de aarde? '))
v = float(input('Geef de snelheid van de satelliet? '))

u = 398600.4418 * pow(10, 9)

#berekening
a = (u * r)/((2 * u) - (r * pow(v, 2)))

periode = 2 * pi * sqrt(pow(a, 3)/ u)

#seconden naar dagen, uren en minuten

aantal_dagen = int(periode // 86400)
tijd_resterend = periode % 86400

aantal_uren = int(tijd_resterend // 3600)
tijd_resterend %= 3600

aantal_minuten = int(tijd_resterend // 60)

#uitvoer
grote_as = 'grote as: {} meter'
periode_seconden = 'periode: {} seconden'
periode_dagen = 'periode: {} dagen, {} uren en {} minuten'

print(grote_as.format(a))
print(periode_seconden.format(periode))
print(periode_dagen.format(aantal_dagen, aantal_uren, aantal_minuten))
