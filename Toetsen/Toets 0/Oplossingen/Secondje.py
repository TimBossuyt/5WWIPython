invoer = int(input("Aantal seconden: "))

seconden = invoer % 60
invoer //= 60
minuten = invoer % 60
invoer //= 60
uren = invoer % 24
dagen = invoer // 24

print(str(dagen) + 'd ' + str(uren) + ':' + str(minuten) + ':' + str(seconden))
