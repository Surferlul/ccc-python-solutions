isPrime = [i%2==1 for i in range(1000001)]
isPrime[1] = False
isPrime[2] = True
l = len(isPrime)
for i in range(3, l, 2):
    if isPrime[i] == False:
        continue
    else:
        for i in range(i*2, l, i):
            isPrime[i] = False
