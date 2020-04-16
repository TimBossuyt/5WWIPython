middagmaal = 5.3
soep = 1.7
vieruurtje = 2.3

def dagprijs(bestelling):
    prijs = 0

    for i in range(len(bestelling)):
        if i % 2 == 0:
            soort = bestelling[i]

            if soort == 'middagmaal':
                prijs += bestelling[i+1] * middagmaal
            elif soort == 'vieruurtje':
                prijs += bestelling[i+1] * vieruurtje
            else:
                prijs += bestelling[i+1] * soep

    return prijs


def weekprijs(bestelling):
    prijs = 0

    for i in range(len(bestelling)):
        prijs += dagprijs(bestelling[i])

    return prijs


print(dagprijs(('soep', 2, 'middagmaal', 2)))