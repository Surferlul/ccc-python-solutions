def execute(prog):
   lines = set()
   location = 0
   while True:
      lines.add(location)
      if location==len(prog)-1: return "success"
      location = findLine(prog, prog[location].split()[-1])
      if location in lines: return "infinite loop"
