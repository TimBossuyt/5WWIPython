#True en False moeten met hoofdletter
#Logische operatoren !!!!!!
# not inverteerd

#getal % 2 == 1 om te testen even / oneven

getal = int(input('Geef getal: '))

if getal < 0:
    if getal % 2 == 0:
        print('Negatief even getal')
    else:
        print('Negatief oneven getal')

elif getal > 0:
    if getal % 2 ==0:
        print('Positief even getal')
    else:
        print('Positief oneven getal')

else:
    print('Getal is 0')



print('Tot ziens')
