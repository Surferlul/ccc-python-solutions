def prod(L):
   for i in L[1:]:
      L[0] *= i
   return L[0]
