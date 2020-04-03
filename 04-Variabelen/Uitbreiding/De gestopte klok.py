#invoer

T1_uur = int(input('Vertrek thuis in uur '))
T1_minuten = int(input('Vertrek thuis in minuten '))

A1_uur = int(input('Aankomst vriendin in uur '))
A1_minuten = int(input('Aankomst vriendin in minuten '))

A2_uur = int(input('Vertrek vriendin in uur '))
A2_minuten = int(input('Vertrek vriendin in minuten '))

T2_uur = int(input('Aankomst thuis in uur '))
T2_minuten = int(input('Aankomst thuis in minuten '))

#-------------------------------------------------------------

#berekening

T1 = T1_uur * 60 + T1_minuten
T2 = T2_uur * 60 + T2_minuten

A1 = A1_uur * 60 + A1_minuten
A2 = A2_uur * 60 + A2_minuten

verstreken_tijd_weg = abs(int(T2 - T1))

verstreken_tijd_vriendin = abs(int(A2 - A1))

reistijd = abs((verstreken_tijd_weg - verstreken_tijd_vriendin)/2)



tussenresultaat = (A2 + reistijd)

juist_uren = int(tussenresultaat // 60)
juist_minuten = int(tussenresultaat % 60)




#----------------------------------------------------------------

print(juist_uren)
print(juist_minuten)
