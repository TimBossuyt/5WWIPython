a = int(input('Getal a: '))
b = int(input('Getal b: '))

som_a = 0
som_b = 0


for i in range(1, a):
    if a % i == 0:
        som_a += i

for i in range(1, b):
    if b % i == 0:
        som_b += i

if som_a  == b and som_b == a:
    uitvoer = '{} en {} zijn bevriende getallen'

else:
    uitvoer ='{} en {} zijn geen bevriende getallen'


print(uitvoer.format(a, b))


