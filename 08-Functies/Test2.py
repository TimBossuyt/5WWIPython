from math import sqrt

def discriminant(a, b, c):
    return (b ** 2) - (4 * a * c)

def wortels (a, b, discriminant):
    w1, w2 = None, None

    if discriminant >= 0:
        w1 = (-b + sqrt(discriminant)) / (2 * a)
        w2 = (-b - sqrt(discriminant)) / (2 * a)

    return w1, w2

wortel1, wortel2 = wortels(2, -1, discriminant(2, -1, -4))

print(wortel1, wortel2)
