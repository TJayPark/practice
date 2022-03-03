def checkDom(start, tar):
  for x,y in zip(start, tar):
    data = x+y
    if(data>5 or data <= 0):
      return False
    return True
N = int(input())
dir = list(input().split(" "))

dic = {'L':(0,-1), 'R':(0,+1), 'U': (-1,0), 'D':(+1,0)}

start = [1, 1]
for D in dir:
  targetD = list(dic[D])
  if(checkDom(start, targetD)):
    start = [x+y for x,y in zip(start, targetD)]

print(start)

