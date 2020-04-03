invoer = input('Kleur: ')

wachtrij = []

while invoer != 'STOP':
    if invoer == '?' and len(wachtrij) > 0:
        print(wachtrij[0])
        wachtrij.remove(wachtrij[0])

    elif invoer != '?':
        wachtrij.append(invoer)

    invoer = input('Kleur: ')


