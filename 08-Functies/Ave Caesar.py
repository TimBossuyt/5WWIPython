def is_kleine_letter(teken):
    return ord(teken) >= ord('a') and ord(teken) <= ord('z')

def is_grote_letter(teken):
    return ord(teken) >= ord('A') and ord(teken) <= ord('Z')

def is_letter(teken):
    return is_kleine_letter(teken) or is_grote_letter(teken)


def roteer_letter(teken, plaatsen):
    if is_kleine_letter(teken):
        ascii = ord(teken) + plaatsen

        if ascii > 122:
            ascii = 96 + (plaatsen - (122- ord(teken)))

    else:
        ascii = ord(teken) + plaatsen

        if ascii > 90:
            ascii = 64 + (plaatsen - (90 - ord(teken)))

    return chr(ascii)


def versleutel(tekst, plaatsen):

    versleutelde_tekst = ''
    for letter in tekst:
        if is_letter(letter):
            versleutelde_tekst += roteer_letter(letter, plaatsen)
        else:
            versleutelde_tekst += letter

    return(versleutelde_tekst)




