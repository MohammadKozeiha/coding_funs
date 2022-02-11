import sys
import math
import numpy as np

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
temp_list_neg = []
temp_list_pos = []
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    if t<0:
        temp_list_neg.append(t)
    if t>0:
        temp_list_pos.append(t)

result = 55526
if temp_list_pos:
    if min(temp_list_pos)<result:
        result = min(temp_list_pos)
if temp_list_neg:
    if min(np.abs(temp_list_neg))<result:
        result = max((temp_list_neg))
if not temp_list_pos and not temp_list_neg:
    result = 0
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(result)
