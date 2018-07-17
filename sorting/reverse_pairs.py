#!/bin/usr/python3

source = [1,2,3,4,5,6,7,8]

mirror = []
for i in range(len(source)-2, -1, -2):
  mirror.extend(source[i:i+2])
    
print(mirror)

i = iter(source)
P = list(zip(i, i))[::-1]
mirror = [x for p in P for x in p]

print(mirror)
