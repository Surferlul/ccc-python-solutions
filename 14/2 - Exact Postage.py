def postalValidate(S):
   S = S.replace(" ", "")
   if len(S) != 6:
      return False
   for i in range (6):
      if i%2:
         if not S[i].isdigit():
            return False
      else:
         if not S[i].isalpha():
            return False
   return S.upper()
