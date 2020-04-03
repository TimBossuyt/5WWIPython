def hint(gok, woord):
    nieuw_woord = ''
    i = 0
    for letter in gok:
        if woord.find(letter) == -1:
            nieuw_woord += '.'

        elif letter == woord[i]:
            nieuw_woord += letter.upper()

        else:
            nieuw_woord += letter
        i += 1

    return nieuw_woord

