def getBASIC():
   res = []
   x=""
   while not "END" in x.split():
      x = input()
      res.append(x)
   return res

def findLine(prog, target):
   for i in prog:
      if i.split()[0] == target:
         return prog.index(i)

def execute(prog):
   lines = set()
   location = 0
   while True:
      lines.add(location)
      if location==len(prog)-1: return "success"
      location = findLine(prog, prog[location].split()[-1])
      if location in lines: return "infinite loop"

if __name__ == "__main__":
   print(execute(getBASIC()))
