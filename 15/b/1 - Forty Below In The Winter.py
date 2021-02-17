temp = input()
temp_num = float (temp[:-1])
if "C" == temp[-1]:
   print(temp_num*9/5+32, "F", sep="")
else:
   print((temp_num-32)*5/9, "C", sep="")
