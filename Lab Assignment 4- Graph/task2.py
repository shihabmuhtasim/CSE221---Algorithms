# -*- coding: utf-8 -*-
"""task2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18EG9CtghMuwc2dY23vDnHB5dk05PendV
"""

#2
from queue import Queue
inp=open("input2.txt", "r")
out=open("output2.txt", "w")
v= inp.readline().split()
r=int(v[0])
con=int(v[1])
mat = [[0 for _ in range(r)] for _ in range(r)]
for i in range(con):
  store=inp.readline().split()
  mat[int(store[0])-1][int(store[1])-1]=1
  mat[int(store[1])-1][int(store[0])-1]=1
s=1
colour=[0]*r
q=Queue()
colour[0]=1
q.put(1)
while not q.empty():
  u=q.get()
  print(u,end=" ", file=out)
  for i in range(r):
    if mat[u-1][i]==1:
      if colour[i]==0:
        colour[i]=1
        q.put(i+1)