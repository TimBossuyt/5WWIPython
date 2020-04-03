def vlag(richting, kleuren):
    uitvoer = ''
    if richting == 'verticaal': #de kleuren staan naast elkaar
        for i in range(len(kleuren)):
            if i == 0:
                uitvoer += kleuren[i] + ' ' + '|'
            elif i == len(kleuren)-1:
                uitvoer += ' ' + kleuren[i]
            else:
                uitvoer += ' ' + kleuren[i] + ' ' + '|'

    else: #de kleuren staan onder elkaar
        for i in range(len(kleuren)):
            if i == len(kleuren)-1:
                uitvoer += kleuren[i]
            else:
                uitvoer += kleuren[i] + '\n'
                uitvoer += '-' + '\n'





    return str(uitvoer)
