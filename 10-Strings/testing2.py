woord = input('woord: ')

for i in range(0, len(woord)):
    if woord[i] in 'aeoui':
        woord[i] = woord[:i] + '*' + woord[i + 1:]

