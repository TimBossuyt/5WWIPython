#invoer
bedrag = float(input('Geef het bedrag: '))

#berekening

aantal_muntstukken = bedrag // 100
eurocent = bedrag % 100

aantal_muntstukken += eurocent // 50
eurocent = eurocent % 50

aantal_muntstukken += eurocent // 20
eurocent = eurocent % 20

aantal_muntstukken += eurocent // 10
eurocent = eurocent % 10

aantal_muntstukken += eurocent // 5
eurocent = eurocent % 5

aantal_muntstukken += eurocent // 2
eurocent = eurocent % 2

aantal_muntstukken += eurocent // 1
eurocent = eurocent % 1

#uitvoer


print(int(bedrag), 'cent kan je omwisselen in', int(aantal_muntstukken), 'muntstukken')
