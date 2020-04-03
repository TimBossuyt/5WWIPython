from random import randint

def gooi_muntstuk():
    rg = randint(0, 2)
    muntstuk = 'munt'
    if rg == 0:
        muntstuk = 'kop'
    return muntstuk

for i in range(10):
    print(gooi_muntstuk())

