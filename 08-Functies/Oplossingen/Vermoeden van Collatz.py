def volgend_collatz_getal(n):
    if n % 2 == 0:
        n /= 2
    else:
        n = (n * 3) + 1

    return int(n)

def collatz(n):
    stap = 1
    while n != 1:
        n = volgend_collatz_getal(n)
        stap += 1

    return stap

