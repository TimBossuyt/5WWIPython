from math import sqrt, floor

#geeft aan of een getal een priemgetal is
# True, getal is een priemgetal, anders False.
def is_priem(getal):
    i = 2
    while i <= floor(sqrt(getal)) and getal % i != 0:
        i += 1

    if i == floor(sqrt(getal)) + 1:
        return True

    else:
        return False #g #


aantal_gevraagd = int(input('aantal gevraagd: '))

som, aantal, n = 0, 0, 2

while aantal < aantal_gevraagd:
 if is_priem(n):
    som, aantal = som + n, aantal + 1

 n += 1

print(som)
