# -*- coding: utf-8 -*-
"""task1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MF8l-aSbcc4ODECRk0JcrVaQJMSj9n-f
"""

#1
inp=open("input1.txt","r")
out=open("output1.txt","w")
x=inp.readline()
n=int(x)
new={}
for i in range(n):
  store=inp.readline().split()
  new[int(store[1])]=store

hold=sorted(new.items())
final=[hold[0][1]]
c=1
current=hold[0][0]

for j in range(1,len(hold)):
  if int(hold[j][1][0])>=current:
    final.append(hold[j][1])
    c+=1
    current=hold[j][0]
print(c,file=out)
for i in range(len(final)):
  print(f"{final[i][0]} {final[i][1]}",file=out)