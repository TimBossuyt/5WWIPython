from operator import itemgetter

def bereken_prijs(artikelen):
    totale_prijs = 0
    for i in range(len(artikelen)):
        totale_prijs += artikelen[i][1]

    return totale_prijs


def winkelbriefje(artikelen):
    winkelartikelen = []
    for i in range(len(artikelen)):
        winkelartikelen.append(artikelen[i][0])

    return winkelartikelen


def sorteer(artikelen):
    artikelen.sort(key=itemgetter(1))

    return artikelen


print(sorteer([('Croky zout', 1.39), ('Milky Way', 3.94)]))

