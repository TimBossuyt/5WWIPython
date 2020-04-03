avogadro = 6.020*10**23
molaire_massa_zwavel = 32.06


#invoer

aantal_mol = float(input('Aantal deeltjes in zwavel? '))

#berekening
aantal_deeltjes = aantal_mol*avogadro

massa = molaire_massa_zwavel*aantal_mol

#uitvoer
print(massa)
print(aantal_deeltjes)
