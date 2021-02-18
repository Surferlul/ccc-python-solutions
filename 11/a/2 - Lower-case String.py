def lowerChar(char):
   if 65 <= ord(char) <= 90:
      return chr(ord(char)+32)
   return char

def lowerString(string):
   out = ""
   for i in range(len(string)):
      out += lowerChar(string[i])
   return out
