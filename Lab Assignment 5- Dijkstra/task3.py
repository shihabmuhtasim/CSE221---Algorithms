# -*- coding: utf-8 -*-
"""task3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RkN-a1AWlJwVRqDFKmou5QqyZO1XBEir
"""

#3
inp=open("input3.txt","r")
out=open("output3.txt","w")
cases=int(inp.readline())
for i in range(cases):
  n,m=inp.readline().split()
  if m=="0":
    print("1",file=out)
  else:
    dic={}
    queue=[]
    extra=[]
    for j in range(int(m)):
      v_1,v_2,edge=inp.readline().split()
      if v_1 not in queue:
        queue.append(v_1)
        extra.append(v_1)
      if v_2 not in queue:
        queue.append(v_2)
        extra.append(v_2)
      if v_1 not in dic:
        dic[v_1]=[(v_2,int(edge))]
      else:
        dic[v_1].append((v_2,int(edge)))
    queue.sort()
    extra.sort()
    # print("DIC",dic)
    # print("QUE",queue)
    # print("EXTRA",extra)   
    #---------------------------
    d=[1000]*len(queue)
    p=[0]*len(queue)
    d[0]=0
    def Not_empty(arr):
      flag=False
      for i in arr:
        if i!=0:
          flag=True
          break
        else:
          flag=False
      return flag

    while Not_empty(queue):
      min=10**10
      idx=None
      for i in range(len(d)):
        if d[i]<min:
          if queue[i]!=0:
            min=d[i]
            idx=i
      u=queue[idx]
      queue[idx]=0 
      d_u=d[idx]
      if u in dic.keys():
        adj=dic[u]
        for tup in adj:
          v_idx=extra.index(tup[0])
          d_v=d[v_idx]
          if d_v>d_u+tup[1]:
            d[v_idx]=d_u+tup[1]
            p[v_idx]=u
      else:
        pass 
    home=n
    last=extra.index(home)
    path=[home]
    val=home
    while val!="1":
      val=p[last]
      path.append(val)
      last=extra.index(val)

    for i in range(len(path)-1,-1,-1):
      print(path[i],end=" ",file=out)
    print("",file=out)