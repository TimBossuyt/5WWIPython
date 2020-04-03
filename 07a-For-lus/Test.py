
naam = input('Naam?')

aantal_klinkers, aantal_medeklinkers = 0, 0 #variabelen in één keer op 0 zetten

for letter in naam:
    if letter in 'aeuoi':
        aantal_klinkers += 1

    else:
        aantal_medeklinkers += 1


print(aantal_klinkers, aantal_medeklinkers)





for letter in naam:
    if letter in 'aeuoi':
        aantal_klinkers += 1

print(aantal_klinkers, len(naam)-aantal_klinkers)
