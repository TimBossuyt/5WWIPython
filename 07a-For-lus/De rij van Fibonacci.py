n = int(input('n-de getal van de rij van Fibonacci: '))

if n <= 2:
    getal = 1


else:

    vorig_1 = 1
    vorig_2 = 1

    for i in range(n-2):
        getal = vorig_1 + vorig_2
        vorig_2 = vorig_1
        vorig_1 = getal


print(getal)

