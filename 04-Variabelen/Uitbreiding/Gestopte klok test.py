#invoer
uur1 = int(input("geef uur: "))
min1 = int(input("geef min: "))

uur2 = int(input("geef uur: "))
min2 = int(input("geef min: "))

uur3 = int(input("geef uur: "))
min3 = int(input("geef min: "))

uur4 = int(input("geef uur: "))
min4 = int(input("geef min: "))

#bereking
y1 = (uur1 * 60) + min1
y2 = (uur2 * 60) + min2
y3 = (uur3 * 60) + min3
y4 = (uur4 * 60) + min4
verstreken_tijd = y4 - y1 #verstreken tijd
verstreken_tijd_vriendin = y3 - y2 #verstreken tijd vriendin
vertrek = verstreken_tijd + (720 - (720 * (verstreken_tijd / abs(verstreken_tijd))))
pauze = verstreken_tijd_vriendin + (720 - (720 * (verstreken_tijd_vriendin / abs(verstreken_tijd_vriendin))))
y5 = (vertrek - pauze) / 2
y6 = y3 + y5
uur_eind = y6 // 60
min_eind = y6 % 60
speciaal = uur_eind - 24
uur_eind -= 12 + (12 * (speciaal/abs(speciaal)))

#uitvoer
print(int(uur_eind))
print(int(min_eind))
