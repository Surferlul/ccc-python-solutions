def countup(n):
   if n>1:
      countup(n - 1)
   else:
      print('Blastoff!')
   print(n)
