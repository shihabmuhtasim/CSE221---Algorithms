# -*- coding: utf-8 -*-
"""task1(a).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eQUfk3n4CyaBX8o_YilPPyhe26rOMoVr
"""

#1 (a)
inputfile=open("/content/drive/MyDrive/Cse221 Lab /Lab assignment 1/input.txt",'r')
output=open("/content/drive/MyDrive/Cse221 Lab /Lab assignment 1/output.txt",'w')
li= inputfile.readlines()
n=int(li[0])
for i in range(1,n+1):
  if int(li[i])%2==0:
    print(f"{int(li[i])} is even", file=output)
  else:
    print(f"{int(li[i])} is odd", file=output)