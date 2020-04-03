aantal_lifters = int(input('Hoeveel lifters: '))

hoogste_score = float(input('Score: '))



for i in range(aantal_lifters - 1):
    for i in range((aantal_lifters // 2) - 1):
        score = float(input('Score: '))
        if score > hoogste_score:
            hoogste_score = score

    if i > aantal_lifters // 2:
        score = float(input('Score: '))
        if score > hoogste_score:
            hoogste_score = score

print(hoogste_score)



