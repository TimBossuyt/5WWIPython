from random import randint

munt = 0 #commit test
aantal_experimenten = 1

for i in range(aantal_experimenten):
    munt += randint(0, 1)

print('munt: ', munt, 'kop: ', aantal_experimenten - munt)

