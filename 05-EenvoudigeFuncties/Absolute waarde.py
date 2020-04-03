
#invoer
willekeurig_1 = float(input('Geef het eerste willekeurig getal '))
willekeurig_2 = float(input('Geef het tweede willekeurig getal '))

#berekening

verschil_1 = abs(abs(willekeurig_1) - abs(willekeurig_2))

verschil_2 = abs(willekeurig_1 - willekeurig_2)

#uitvoer
uitvoer = '{:.4f} \N{LESS-THAN OR EQUAL TO} {:.4f}'

print(uitvoer.format(verschil_1, verschil_2))
