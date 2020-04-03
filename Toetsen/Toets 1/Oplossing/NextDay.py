d = int(input('dag: '))
m = int(input('maand: '))
j = int(input('jaar: '))

dagen_in_maand = 31

if m == 4 or m == 6 or m == 9 or m == 11:
    dagen_in_maand = 30
elif m == 2:
    if (j % 4 == 0 and j % 100 != 0) or j % 400 == 0:
        dagen_in_maand = 29
    else:
        dagen_in_maand = 28

d += 1

if d > dagen_in_maand:
    d = 1
    m += 1

if m > 12:
    m = 1
    j += 1

print(d, m, j, sep='/')

