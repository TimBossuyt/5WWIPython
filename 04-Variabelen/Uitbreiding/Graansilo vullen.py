import math

#invoer
breedte = float(input('Breedte veld? '))
lengte = float(input('Lengte veld? '))

graanwinst = float(input('Kubieke meter graan per hectare? '))

straal = float(input('Straal van de silo? '))
hoogte = float(input('Hoogte van de silo? '))

pi = 3.1415926535


#berekening
oppervlakte_hectare = (lengte * breedte) / 10000
inhoud_silo = pi * straal**2 * hoogte

oogst = oppervlakte_hectare * graanwinst

aantal_gevulde_silo = math.ceil(round(oogst / inhoud_silo, 3))

volume_over = oogst - ((aantal_gevulde_silo - 1 ) * inhoud_silo)

hoogte_silo_over = (volume_over) / (pi * (straal**2))


#uitvoer
print(int(aantal_gevulde_silo))
print(hoogte_silo_over)

