#invoer
afstand = float(input('Geef de afstand tussen de twee puntladingen: '))
k = 8.99**9
q1 = 2.0**-6
q2 = 1.0**-6

#berekening
afstand = afstand * 10**-2
teller = k * q1 * q2
noemer = afstand**2
coulombkracht = teller/noemer

#uitvoer
print(coulombkracht)


