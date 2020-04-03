def hint(gok, oplossing):
    hint = ''

    for i in range(0, len(oplossing)):
        if oplossing.find(gok[i]) != -1:
            if gok[i] == oplossing[i]:
                hint += gok[i].upper()
            else:
                hint += gok[i].lower() #lower moet niet maar is voor de zekerheid
        else:
            hint += '.'

    return hint


print(hint('absec', 'aceet'))
