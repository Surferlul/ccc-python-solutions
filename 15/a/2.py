def findLine(prog, target):
   for i in prog:
      if i.split()[0] == target:
         return prog.index(i)
