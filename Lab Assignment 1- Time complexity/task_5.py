# -*- coding: utf-8 -*-
"""task 5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ndu9yfrndAFAlqGpuxcpPIrCxyIO9gbl
"""

#5
inputfile=open("/content/drive/MyDrive/Cse221 Lab /Lab assignment 1/input5.txt",'r')
output=open("/content/drive/MyDrive/Cse221 Lab /Lab assignment 1/output5.txt",'w')
n=inputfile.readline()
li=inputfile.readlines()
name=[]
loc=[]
time=[]
for line in range(int(n)):
  temp=li[line].split()
  name.append(temp[0])
  loc.append(temp[4])
  time.append(temp[6])
#---------------
for i in range(len(name)-1):
  for j in range(i+1, len(name)):
    if name[i]>name[j]:
      name[i],name[j] = name[j],name[i]
      loc[i],loc[j] = loc[j],loc[i]
      time[i],time[j] = time[j],time[i]

#--------------------------------
for i in range(len(name)-1):
  min=i
  for j in range(i+1,len(name)):
    if name[i]!=name[j]:
      break
    else:
      one=time[i].replace(':', '')
      two=time[j].replace(':', '')
      if int(one)<int(two):
        min=j
  name[i],name[min] = name[min],name[i]
  loc[i],loc[min] = loc[min],loc[i]
  time[i],time[min] = time[min],time[i]

#-------------------------------
strin=""
for i in range(len(name)):
  strin+= f"{name[i]} will departure for {loc[i]} at {time[i]}\n"

print(strin, file=output)