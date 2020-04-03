def ik_heb_gemoord(opdrachtenlijst, moordenaar):
    if len(opdrachtenlijst) != 1:
        index = opdrachtenlijst.index(moordenaar)
        slachtoffer_index = index + 1

        opdrachtenlijst.pop(slachtoffer_index % len(opdrachtenlijst))

    return opdrachtenlijst[(opdrachtenlijst.index(moordenaar) + 1) % len(opdrachtenlijst)], opdrachtenlijst


def ik_ben_vermoord(opdrachtenlijst, slachtoffer):
    index = opdrachtenlijst.index(slachtoffer)
    if len(opdrachtenlijst) != 1:
        opdrachtenlijst.pop(index)

    nieuw_slachtoffer = index % len(opdrachtenlijst)

    return opdrachtenlijst[nieuw_slachtoffer], opdrachtenlijst
