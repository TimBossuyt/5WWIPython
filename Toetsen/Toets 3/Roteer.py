def roteer(woord, aantal):
    nieuw_woord = ''
    for letter in woord:
        index = woord.find(letter) + aantal

        if index > len(woord)-1:
            while index > len(woord)-1:
                index -= len(woord)

        nieuw_woord += woord[index]

    return nieuw_woord


