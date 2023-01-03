

#2
inp=open('r',"C:\Users\USER\Dropbox\1. STUDIEOS\CSE221\Lab ass\Lab Assignment 6\input2.txt")
out=open("output2.txt","w")
temp=inp.readline().split()
n=int(temp[0])
m=int(temp[1])
new={}
for i in range(n):
  store=inp.readline().split()
  #print(store)
  if int(store[0]) in new.keys():
    new[int(store[0])].append((store[0],store[1]))
  else:
    new[int(store[0])]=[(store[0],store[1])]
print(new)
hold=sorted(new.items())
print(hold)
arr=[]
for i in range(len(hold)):
  if len(hold[i][1])>1:
    for j in range(len(hold[i][1])):
      ap=(hold[i][0],hold[i][1][j])
      arr.append(ap)
  else:
    ap=(hold[i][0],hold[i][1][0])
    arr.append(ap)
print(arr)
c=1
end_a=int(arr[0][1][1])
end_b=0
for j in range(1,len(arr)):
  if end_a<=arr[j][0]:
    c+=1
    end_a=int(arr[j][1][1])
  elif end_b<=arr[j][0]:
    c+=1
    end_b=int(arr[j][1][1])
  else:
    pass
print(c)