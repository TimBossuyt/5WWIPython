getal = int(input('Geef een getal: '))
bereik = int(100/getal + 1)
veelvouden = 0

for i in range(bereik):
    veelvouden = ((i * getal) + veelvouden)

print(veelvouden)
#veelvouden
