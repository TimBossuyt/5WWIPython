def germaniseer(zin):
    nieuwe_zin = ''
    #overloop alle letters van de string
    for i in range(0, len(zin)):
        #indien de letter een spatie is
        if zin[i] == ' ':
            nieuwe_zin += (' ' + zin[i+1].upper())

        elif zin[i - 1] != ' ':
            nieuwe_zin += zin[i]

    return nieuwe_zin





