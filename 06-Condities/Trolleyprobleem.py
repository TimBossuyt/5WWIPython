antwoord_1 = input('Trek aan de hendel van de wissel? ')
antwoord_2 = input('Man van de brug duwen? ')

if antwoord_1 == 'ja' and antwoord_2 == 'ja':
    doden = 2

elif antwoord_1 == 'ja' and antwoord_2 == 'nee':
    doden = 1

elif antwoord_1 == 'nee' and antwoord_2 == 'ja':
    doden = 1

elif antwoord_1 == 'nee' and antwoord_2 == 'nee':
    doden = 5

print(doden)

#dit is gemakkelijker

if antwoord_1 != antwoord_2:
    doden = 1

elif antwoord_1 == 'ja':
    doden = 2

else:
    doden = 5


