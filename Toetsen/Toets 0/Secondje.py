#invoer
aantal_seconden = float(input('Geef een aantal gehele seconden: '))

#berekening
dagen = int(aantal_seconden // 86400)
tijd_resterend = aantal_seconden % 86400

uren = int(tijd_resterend // 3600)
tijd_resterend %= 3600

minuten = int(tijd_resterend // 60)
tijd_resterend %= 60

seconden = int(tijd_resterend)

#uitvoer
print(str(dagen) + 'd', str(uren) + ':' + str(minuten) + ':' + str(seconden))
