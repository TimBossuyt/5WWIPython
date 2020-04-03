from math import pi, sin, cos

getal = float(input('Geef een getal: '))

x, y = 0, 0

for i in getal:
    if i != '.':
        x += cos((pi / 2) - (i * 0.2*pi))

        y += cos( i * 0.2 * pi)


print(x, y)
