timbitsLeft = int(input())
totalCost = 0

bigBoxes = int(timbitsLeft / 40)
totalCost = bigBoxes * 6.19
timbitsLeft -= 40 * bigBoxes

if timbitsLeft >= 20:
    totalCost += 3.39
    timbitsLeft -= 20
if timbitsLeft >= 10:
    totalCost += 1.99
    timbitsLeft -= 10

totalCost += timbitsLeft * 0.20
print(totalCost)
