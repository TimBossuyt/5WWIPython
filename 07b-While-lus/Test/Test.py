vorst_periode = 0

#1e invoerwaarde VOOR while-lus
temperatuur = int(input('Dagtemperatuur: '))

while temperatuur <= 0:
    vorst_periode += 1
    temperatuur = int(input('Dagtemperatuur: '))

print(vorst_periode)
