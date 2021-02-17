temp = input()
if "C" in temp:
   temp = float (temp[:-1])
   print(temp*9/5+32, "F", sep="")
else:
   temp = float (temp[:-1])
   print((temp-32)*5/9, "C", sep="")
