# -*- coding: utf-8 -*-
"""task4(a).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iKGTVDL2uvsbxF4T_D2OFVS42xOrUAXe
"""

input = open('input4.txt', 'r')
out= open("output4(a).txt","w")
read = (input.readlines())
store = [] #initial checking 
for i in read:
  temp=i.strip()
  s_li=temp.split()
  store.append(s_li)    
b_queue = [] #initialize queue 

def b_checker():
    for i in store:
        if i[1] =='doctor':
            seedoctor()
        else:
            enque(i)

def seedoctor():
    for i in range(len(b_queue)):
        for j in range(len(b_queue)-1):
            if  int(b_queue[j+1][1])<int(b_queue[j][1]):
                b_queue[j+1], b_queue[j] = b_queue[j], b_queue[j+1]
    print("See Doctor:",b_queue[0][0],file=out)
    remove =b_queue.pop(0)

def enque(name):
    b_queue.append(name)

def printqueue(arr):
  for i in arr:
        print('Name:',i[0])    

b_checker()
#printqueue(b_queue)