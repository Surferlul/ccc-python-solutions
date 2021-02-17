def digitalRoot(n):
   if n<10:
      return n
   else:
      return digitalRoot(digitalSum(n))
