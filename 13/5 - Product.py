def prod(L):
   for i in range(1,len(L)):
      L[0] *= L[i]
   return L[0]
