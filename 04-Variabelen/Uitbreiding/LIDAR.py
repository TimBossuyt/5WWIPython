#invoer
tijd_seconden = float(input('Geef het aantal nanoseconden: ')) * 10**-9

c = 299792458
n = 1.000277

#berekening

afstand_meter = (c * tijd_seconden) / (2 * n)

#uitvoer

print(afstand_meter, 'meter')
