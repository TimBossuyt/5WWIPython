populatiedichtheid = float(input('Populatiedichtheid: '))

vruchtbaarheidsparameter = float(input('Vruchtbaarheidsparameter: '))

aantal_tijdstippen = int(input('Aantal tijdstippen: '))

populatie = populatiedichtheid

print(populatie)

for i in range(aantal_tijdstippen - 1):
        populatie = vruchtbaarheidsparameter * populatiedichtheid*(1 - populatiedichtheid)

        populatiedichtheid = populatie

        print(populatie)







