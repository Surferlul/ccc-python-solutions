def digitalSum(n):
   if n < 10:
      return n
   else:
      return digitalSum(n//10) + n%10
