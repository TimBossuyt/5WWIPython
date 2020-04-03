bruto_jaarsalaris = float(input('Bruto jaarsalaris: '))



rsz_bijdrage = bruto_jaarsalaris * 0.1307

netto_belastbaar_inkomen = float(bruto_jaarsalaris - rsz_bijdrage)

if netto_belastbaar_inkomen <= 8860: #geen belastingen
    netto_jaarsalaris = netto_belastbaar_inkomen

#verdeling over de schijven

#schijf 1 vullen
if netto_belastbaar_inkomen - 13250 < 0: #schijf is niet volledig gevuld
    belastingen_wel = netto_belastbaar_inkomen - 8860

    voorheffing1 = belastingen_wel * 0.25
    voorheffing = voorheffing1

else: #schijf is volledig gevuld
    voorheffing1 = 1097.50
    salaris_resterend = netto_belastbaar_inkomen - 13250
    voorheffing = voorheffing1

    if salaris_resterend - 10140 < 0: #schijf 2 is niet volledig gevuld
        voorheffing2 = salaris_resterend * 0.40
        voorheffing = voorheffing1 + voorheffing2

    else: #schijf is volledig gevuld
        voorheffing2 = 4056
        salaris_resterend -= 10140
        voorheffing = voorheffing1 + voorheffing2

        if salaris_resterend - 17090 < 0: #schijf 3 is niet volledig gevuld
            voorheffing3 = salaris_resterend * 0.4500
            voorheffing = voorheffing1 + voorheffing2 + voorheffing3

        else: #schijf 3 is volledig gevuld
            voorheffing3 = 7690
            salaris_resterend -= 17090

            voorheffing4 = salaris_resterend * 0.50
            voorheffing = voorheffing1 + voorheffing2 + voorheffing3 + voorheffing4



netto_jaarsalaris = netto_belastbaar_inkomen - voorheffing

#___________________________

uitvoer_1 = '+ bruto jaarsalaris {:>10.2f}'
uitvoer_2 = '- rsz               {:>10.2f}'
uitvoer_3 = '- voorheffing       {:>10.2f}'
uitvoer_4 = '=============================='
uitvoer_5 = '+ netto jaarsalaris {:>10.2f}'
uitvoer_6 = '+ netto maandsalaris {:>9.2f}'

print(uitvoer_1.format(bruto_jaarsalaris))
print(uitvoer_2.format(rsz_bijdrage))
print(uitvoer_3.format(voorheffing))
print(uitvoer_4)
print(uitvoer_5.format(netto_jaarsalaris))
print(uitvoer_6.format(netto_jaarsalaris/12))
