bruto_salaris = float(input('Bruto jaarsalaris? '))
rsz = bruto_salaris * 0.1307
netto_belastbaar = bruto_salaris - rsz

schijf_1 = max(min(netto_belastbaar, 13250) - 8860, 0) * 0.25
schijf_2 = max(min(netto_belastbaar, 23390) - 13250.01, 0) * 0.4
schijf_3 = max(min(netto_belastbaar, 40480) - 23390.01, 0) * 0.45
schijf_4 = max(netto_belastbaar - 40480.01, 0) * 0.5

voorheffing = schijf_1 + schijf_2 + schijf_3 + schijf_4
netto_inkomen = netto_belastbaar - voorheffing

uitvoer = '{:<20}{:>10.2f}'

print(uitvoer.format('+ bruto jaarsalaris', bruto_salaris))
print(uitvoer.format('- rsz', rsz))
print(uitvoer.format('- voorheffing', voorheffing))
print(30 * '=')
print(uitvoer.format('+ netto jaarsalaris', netto_inkomen))
print(uitvoer.format('+ netto maandsalaris', netto_inkomen / 12))

