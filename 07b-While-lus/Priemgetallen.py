getal = int(input('Geef een getal: '))

i = 2

if getal == 1:
    print('1 is geen priemgetal')

else:
    while getal % i != 0 and getal != i:
        i += 1

    if getal == i:
        print(getal, 'is een priemgetal')

    else:
        print(getal, 'is geen priemgetal')



