import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input()
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
A = ord('A')
Z = ord('Z')
a = ord('a')
z = ord('z')
for i in range(h):    
    row = input()    
    j = 0
    result = ""
    while j < len(t):
        x = ord(t[j])
        if x in range(A, Z+1) : x = x - A
        elif x in range(a, z+1) : x = x - a
        else: x = len(row) // 4 - 1
        result = result + row[l*x:l*(x+1)]
        j = j+1
    print(result)
