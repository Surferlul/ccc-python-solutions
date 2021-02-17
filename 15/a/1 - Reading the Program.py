def getBASIC():
   res = []
   x=""
   while not "END" in x.split():
      x = input()
      res.append(x)
   return res
