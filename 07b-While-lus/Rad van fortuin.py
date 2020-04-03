gevraagde_woord = input('Woord: ')
totaal = 0

gegokte_letters = ''

gedraaide_geldbedrag = int(input('Gedraaide geldbedrag: '))

letter = input('Geef een letter: ')

while letter in gevraagde_woord and not letter in gegokte_letters:
    gegokte_letters += letter
    totaal += gedraaide_geldbedrag

    letter = input('Geef een letter: ')

print(totaal)

