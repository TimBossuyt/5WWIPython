def dubbels(lijst):
    nieuwe_lijst = []
    for term in lijst:
        if lijst.count(term) > 1 and term not in nieuwe_lijst:
            nieuwe_lijst.append(term)


    return nieuwe_lijst
