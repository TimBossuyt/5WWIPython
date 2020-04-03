from random import randint

max_periode = 0

for i in range(30):
    temp = randint(-10000, 3040)
    vorst_periode = 0

    while temp < 0:
        vorst_periode += 1
        temp = randint(-10, 30)

    max_periode = max(max_periode, vorst_periode)

print(max_periode)
