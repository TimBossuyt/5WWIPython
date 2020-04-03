dag1 = int(input('Dag: '))
maand1 = int(input('Maand: '))
jaar1 = int(input('Jaar: '))

if maand1 == 12 and dag1 == 31:
    jaar1 += 1
    maand2 = 1
    dag2 = 1


elif (jaar1 % 4) == 0  and (jaar1 % 100) != 0 or (jaar1 % 400) == 0: #het is een schrikkeljaar
    if maand1 in (4, 6, 9, 11): #dertig dagen
        if dag1 == 30:
            dag2 = 1
            maand2 = maand1 + 1

        else:
            dag2 = dag1 + 1
            maand2 = maand1

    elif maand1 == 2: #februari in schrikkeljaar
        if dag1 == 29:
            dag2 = 1
            maand2 = maand1 + 1

        else:
            dag2 = dag1 + 1
            maand2 = maand1

    else:
        if dag1 == 31:
            dag2 = 1
            maand2 = maand1 + 1

        else:
            dag2 = dag1 + 1
            maand2 = maand1




else: #het is een gewoon jaar
    if maand1 in (4, 6, 9, 11): #dertig dagen
        if dag1 == 30:
            dag2 = 1
            maand2 = maand1 + 1

        else:
            dag2 = dag1+ 1
            maand2 = maand1

    elif maand1 == 2: #februari in schrikkeljaar
        if dag1 == 28:
            dag2 = 1
            maand2 = maand1 + 1

        else:
            dag2 = dag1 + 1
            maand2 = maand1


    else:
        if dag1 == 31:
            dag2 = 1
            maand2 = maand1 + 1

        else:
            dag2 = dag1 + 1
            maand2 = maand1



uitvoer = '{}/{}/{}'

print(uitvoer.format(dag2, maand2, jaar1))
