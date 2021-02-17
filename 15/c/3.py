def move(txt, x):
   txt = [ord(i) for i in txt]
   for i in range(len(txt)):
      if ord("A") <= txt[i] <= ord("Z"):
         txt[i] += x
         txt[i] = (txt[i] - ord("A")) % 26 + ord("A")
   return "".join ([chr(i) for i in txt])

def goodness(txt):
   res = 0
   for i in txt:
      if i.isalpha():
         res += letterGoodness[ord(i)-ord("A")]
   return res

def best_match(txt):
   best = ["", 0]

   for i in range(26):
      txt = move(txt, 1)
      gdnss = goodness(txt)
      if gdnss > best[1]:
         best[0] = txt
         best[1] = gdnss
   
   return best[0]

print(best_match(input()))
   
         
