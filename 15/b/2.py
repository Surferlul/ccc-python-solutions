def check(S):
   if len (S.replace(" ", "")) != 16:
      return False
   for i in range(len(S)):
      if i%5==4:
         if S[i] != " ":
            return False
      else:
         if not S[i].isdigit():
            return False
         
   x = 0
   for i in S.replace(" ", ""):
      x += int(i)
   if not x%10:
      return True
   return False
