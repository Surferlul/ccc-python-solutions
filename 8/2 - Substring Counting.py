needle = input()
haystack = input()
x = 0
for i in range(len(haystack)-len(needle) + 1):
   if haystack[:len(needle)] == needle:
      x += 1
   haystack = haystack[1:]
print(x)
