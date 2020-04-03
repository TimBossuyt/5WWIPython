windsnelheid = int(input('Geef de windsnelheid in km/h: '))

if windsnelheid < 119:
    categorie = 'geen orkaan'

elif windsnelheid >= 119 and windsnelheid <= 153:
    categorie = 'categorie 1'

elif windsnelheid <= 177:
    categorie = 'categorie 2'

elif windsnelheid <= 209:
    categorie = 'categorie 3'

elif windsnelheid <= 249:
    categorie = 'categorie 4'

else:
    categorie = 'categorie 5'



print(categorie)

