txt = input().lower().split()
while txt[-1] != "###":
   txt += input().lower().split()
m = [0]*len(txt)
for i in range(len(txt)):
   m[i]=txt.count(txt[i])
print(txt[m.index(max(m))])
