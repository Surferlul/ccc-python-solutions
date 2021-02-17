def nestedListContains(NL, target):
   if isinstance(NL, int):
      if NL == target:
         return True
      return False
   for i in NL:
      if nestedListContains(i, target):
         return True
   return False
