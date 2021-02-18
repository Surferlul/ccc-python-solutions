width = int(input())
while True:
   i = input()
   if i == "END":
      break
   print("."* ((width - len(i) + 1) // 2) + i + "."* ((width - len(i)) // 2))
