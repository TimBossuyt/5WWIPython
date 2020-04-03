score_thuis = int(input('Geef de gemaakte punten van de thuisploeg '))
score_uit = int(input('Geef de gemaakte punten van de uitploeg: '))

verschil = score_thuis - score_uit

if verschil > 0:  #team thuis is gewonnen
    if verschil < 10:
        punten_thuis = 600 - 70
        punten_uit = 400 + 70

    elif verschil >= 10 and verschil < 20 :
        punten_thuis = 700 - 70
        punten_uit = 300 + 70

    else:
        punten_thuis = 800 - 70
        punten_uit = 200 + 70

else:  #team uit is gewonnen
    verschil = abs(verschil)
    if verschil < 10:
        punten_uit = 600 + 70
        punten_thuis = 400 - 70

    elif verschil >= 10 and verschil < 20 :
        punten_uit = 700 + 70
        punten_thuis = 300 - 70

    else:
        punten_uit = 800 + 70
        punten_thuis = 200 - 70

uitvoer_thuis = 'thuisploeg: {:.2f}'
uitvoer_uit = '  uitploeg: {:.2f}'

print(uitvoer_thuis.format(punten_thuis))
print(uitvoer_uit.format(punten_uit))


