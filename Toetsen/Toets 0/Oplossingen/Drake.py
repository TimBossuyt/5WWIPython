
# https://en.wikipedia.org/wiki/Drake_equation
# https://www.youtube.com/watch?v=qMybbu_1hAY
r = 2
f_c = 0.2

# kans op intelligent leven: l_i = f_p * n_e * f_1
l_i = float(input('kans op ontwikkeling van leven op een planeet: '))
f_i = float(input('kans op evolutie naar intelligent leven: '))
l = float(input('jaren nodig voor het versturen van een detecteerbaar signaal: '))

n = r * l_i * f_i * f_c * l

print('samenlevingen in de melkweg waarmee we zouden kunnen communiceren: ', int(n))
