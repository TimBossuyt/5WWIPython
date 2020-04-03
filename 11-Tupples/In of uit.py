from math import sqrt

def binnen_of_buiten(p, q, t):
    afstand_middelpunt = sqrt((p[0]-t[0])**2 + (p[1]-t[1])**2)
    straal_cirkel = sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2)

    if afstand_middelpunt == straal_cirkel:
        plaats = 'op'
        afstand = straal_cirkel

    elif afstand_middelpunt < straal_cirkel:
        plaats = 'binnen'
        afstand = afstand_middelpunt
    else:
        plaats = 'buiten'
        afstand = afstand_middelpunt
    return (plaats, round(afstand, 4))



