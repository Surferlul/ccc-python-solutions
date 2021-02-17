txt = input().split()
while txt[-1] != "###":
   txt += input().split()
amount = {}
for i in txt:
   if i.lower() in amount:
      amount[i.lower()] += 1
   else:
      amount[i.lower()] = 1
max = ["", 0]
for i in amount:
   if amount[i] > max[1]:
      max = [i, amount[i]]
   else:
      pass
print(max[0])
