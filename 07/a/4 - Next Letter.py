char = input()
if ord(char) == ord("Z"):
   print("A")
else:
   print(chr(ord(char) + 1))
# without if:
# print(chr((ord(input()) - ord("A") + 1) % 26 + ord("A")))
