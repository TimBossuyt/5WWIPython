a_dobbelsteen_1 = int(input('Wat is de uitslag van de eerste dobbelsteen? '))
a_dobbelsteen_2 = int(input('Wat is de uitslag van de tweede dobbelsteen? '))
a_dobbelsteen_3 = int(input('Wat is de uitslag van de derde dobbelsteen? '))

v_dobbelsteen_1 = int(input('Wat is de uitslag van de eerste dobbelsteen? '))
v_dobbelsteen_2 = int(input('Wat is de uitslag van de tweede dobbelsteen? '))

a_grootste_waarde = max(a_dobbelsteen_1, a_dobbelsteen_2, a_dobbelsteen_3)
a_kleinste_waarde = min(a_dobbelsteen_1, a_dobbelsteen_2, a_dobbelsteen_3)
a_middenste_waarde = int((a_dobbelsteen_1 + a_dobbelsteen_2 + a_dobbelsteen_3) - (a_kleinste_waarde + a_grootste_waarde))

v_grootste_waarde = max(v_dobbelsteen_1, v_dobbelsteen_2)
v_kleinste_waarde = min(v_dobbelsteen_2, v_dobbelsteen_1)

a_verloren_legers = 0
v_verloren_legers = 0


#berekening
if a_grootste_waarde == v_grootste_waarde:
    a_verloren_legers += 1

if a_middenste_waarde == v_kleinste_waarde:
    a_verloren_legers += 1

if a_grootste_waarde > v_grootste_waarde:
    v_verloren_legers += 1

elif a_grootste_waarde < v_grootste_waarde:
    a_verloren_legers += 1

if a_middenste_waarde > v_kleinste_waarde:
    v_verloren_legers += 1

elif a_middenste_waarde < v_kleinste_waarde:
    a_verloren_legers += 1


if a_verloren_legers != 1 and v_verloren_legers != 1:
    uitslag = 'aanvaller verliest {} legers, verdediger verliest {} legers'


elif a_verloren_legers!= 1 and v_verloren_legers == 1:
    uitslag = 'aanvaller verliest {} legers, verdediger verliest {} leger'

elif a_verloren_legers == 1 and v_verloren_legers == 1:
    uitslag = 'aanvaller verliest {} leger, verdediger verliest {} leger'

elif a_verloren_legers != 1 and v_verloren_legers == 1:
    uitslag = 'aanvaller verliest {} legers, verdediger verliest {} leger'



print(uitslag.format(a_verloren_legers, v_verloren_legers))
