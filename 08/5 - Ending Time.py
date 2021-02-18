t = input()
D = int(input())
h = int(t[:2])
m = int(t[3:])
m += D
h += m//60
m = str(m%60)
m = "0" * (2-len(m)) + m
h = str(h%24)
h = "0" * (2-len(h)) + h
print(h + ":" + m)
