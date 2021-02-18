res = ""
for i in range(2, 8):
   chars = "chr:  "
   nums = "asc: "
   for j in range(16):
      chars += chr(16*i+j) + "   "
      nums += str(16*i+j) + " " * (4-len(str(16*i+j)))
   res += chars + "\n" + nums + "\n"
print(res[:-1])
