def choose(n, k):
   res = n/k
   while k > 1:
      n-= 1
      k -= 1
      res *= n/k
   return res
