letter = input()
if ord("A") <= ord(letter) <= ord("Z"):
   print(ord(letter)-ord("A")+1)
else:
   print("invalid")
