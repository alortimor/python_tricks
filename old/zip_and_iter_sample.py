#!/usr/bin/python3
# Comment

if __name__ == "__main__":
  source=[1,2,3,4,5,6,7,8]

  print(source[::-1])

  i = iter(source)
  x = zip(i,i)
  i = iter(source)
  q = zip(i,i)
  for l in q:
    print(l)

  i = iter(source)
  P = list(zip(i, i))[::-1]
  print(P)
  mirror = [x for p in P for x in p] 
