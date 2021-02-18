def replace(l, X, Y):
   while X in l:
      i = l.index(X)
      l.pop(i)
      l.insert(i, Y)
