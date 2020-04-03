def verwijder_medeklinkers(woord):
    nieuw_woord = ''
    index = -max(woord.find('a'), woord.find('e'), woord.find('i'), woord.find('o'), woord.find('u'))

    if woord[0] == 'a' or woord[0] == 'e' or woord[0] == 'i' or woord[0] == 'o' or woord[0] == 'u':
        nieuw_woord = woord

    else:
        nieuw_woord += woord[index:]


    return nieuw_woord


def varkenslatijn(woord):
    nieuw_woord = ''


    if woord[0] == 'a' or woord[0] == 'e' or woord[0] == 'i' or woord[0] == 'o' or woord[0] == 'u':
        nieuw_woord += (woord + 'ibus')


    elif woord[len(woord)-1] == 'a' or woord[len(woord)-1] == 'i' or woord[len(woord)-1] == 'u':
        nieuw_woord += (woord + 'nt')

    else:
        nieuw_woord += verwijder_medeklinkers(woord)

    nieuw_woord.replace('j', 'i')
    nieuw_woord.replace('x', '')
    nieuw_woord.replace('y', '')


    return nieuw_woord

def vertaal(zin):
    pass
