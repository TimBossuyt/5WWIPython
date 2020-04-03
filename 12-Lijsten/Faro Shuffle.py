def nieuw_kaartspel(kleuren, waarden):
    lijst = []

    for kleur in kleuren:
        for waarde in waarden:
            lijst.append(str(kleur + waarde))

    return lijst


