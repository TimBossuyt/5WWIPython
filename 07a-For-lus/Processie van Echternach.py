t = int(input('Tijdstip: '))

afstand = 0
stappen_voor = 0
stappen_achter = 0
for i in range(1, t+1):
    if i%2 != 0:
        stappen_voor += 2
        afstand += stappen_voor

    elif i%2 == 0:
        stappen_achter = (stappen_voor/2)
        afstand -= stappen_achter




uitvoer = '{:.0f}'
print(uitvoer.format(afstand))
