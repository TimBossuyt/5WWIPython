#13,12 + 0,6215T - 11.37W^0,16 + 0.3965TW^16


#invoer
temperatuur = float(input('Geef de temperatuur in graden Celsius: '))
windsnelheid = float(input('Geef de windsnelheid in km/h: '))

#berekening
gevoelstemperatuur = 13.12 + 0.6215 * temperatuur - 11.37 * pow(windsnelheid, 0.16) + 0.3965 * temperatuur * pow(windsnelheid, 0.16)

#uitvoer
print(gevoelstemperatuur)
