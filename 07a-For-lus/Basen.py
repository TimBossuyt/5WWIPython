aantal_basen = int(input('Aantal basen: '))
type_a = 0
type_t = 0
type_g = 0
type_c = 0

basen = ''

for i in range(aantal_basen):
    type = str(input('Type base: '))

    if 'A' in type:
        type_a = 1
        basen = 'A '

    elif 'T' in type:
        type_t = 1
        basen = 'T '

    elif 'G' in type:
        type_g = 1
        basen = 'G '

    elif 'C' in type:
        type_c = 1
        basen = 'C '

aantal_types = type_a + type_c + type_g + type_t

uitvoer = 'De DNA-keting bevat {} verschillende soorten basen: {}'

print(uitvoer.format(aantal_types, basen))








