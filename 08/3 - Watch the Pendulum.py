from math import cos
L = float(input())
A = float(input())
for T in range(10):
   print( L * cos(A * cos(T * (9.8/L)**0.5)) - L * cos(A))
