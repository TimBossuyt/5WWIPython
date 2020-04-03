snelheid_stijn = int(input('De snelheid van Stijn (in m/s): '))
snelheid_kaat = int(input('De snelheid van Kaat (in m/s): '))

afstand_stijn = 0
afstand_kaat = 0

afstand = int(input('Wat is de afstand tussen de 2 huizen: '))

seconden = 0

while (afstand_stijn + afstand_kaat) < afstand:
    afstand_stijn += snelheid_stijn
    afstand_kaat += snelheid_kaat

    seconden += 1

uitvoer = 'Na {} s hebben Stijn en Kaat elkaar ontmoet.'

print(uitvoer.format(seconden))
