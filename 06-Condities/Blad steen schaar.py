speler_1 = input('Blad, steen of schaar? ')
speler_2 = input('Blad, steen of schaar? ')

if speler_1 == speler_2: #gelijk
    uitvoer = 'onbeslist'

elif speler_1 == 'steen' and speler_2 == 'blad': #speler 2 is gewonnen
    uitvoer = 'speler 2 wint'

elif speler_1 == 'steen' and speler_2 == 'schaar': #speler 1 is gewonnen
    uitvoer = 'speler 1 wint'

elif speler_1 == 'blad' and speler_2 == 'schaar': #speler 2 is gewonnen
    uitvoer = 'speler 2 wint'

elif speler_1 == 'blad' and speler_2 == 'steen': #speler 1 is gewonnen
    uitvoer = 'speler 1 wint'

elif speler_1 == 'schaar' and speler_2 == 'steen': #speler 2 is gewonnen
    uitvoer = 'speler 2 wint'

else: #speler 1 is gewonnen
    uitvoer = 'speler 1 wint'

print(uitvoer)
#speler 1 berekenen om te winnen, else speler 2 wint
