def lowerChar(char):
   if 65 <= ord(char) <= 90:
      return chr(ord(char)+32)
   return char
