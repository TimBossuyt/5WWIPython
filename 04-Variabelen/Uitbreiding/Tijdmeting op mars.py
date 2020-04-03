
#invoer
factor = 24.65979

aantal_sol = int(input('Geef het aantal sol? '))

aantal_uren = aantal_sol * factor

#omzet van 10-delig naar 60 delig

uur_zonder = int(aantal_uren)

rest_minuten = round(aantal_uren - uur_zonder, 5) *3600

minuten = int(rest_minuten // 60)

seconden = int(rest_minuten % 60)

aantal_dagen = uur_zonder // 24

uur = uur_zonder % 24


#uitvoer
print(aantal_sol, 'sol =', aantal_dagen, 'dagen,', uur, 'uren,', minuten, 'minuten en', seconden, 'seconden' )




