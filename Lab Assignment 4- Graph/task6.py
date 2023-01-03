# -*- coding: utf-8 -*-
"""task6

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/199U-zJtN8WjGjkw8FS4-8Yjzvp6qJuxU
"""

#6
inp = open("input6.txt", "r")
out=open("output6.txt", "w")
full = inp.read().splitlines()
temp=full[0].split()
a=int(temp[0])
b=int(temp[1])
mat1=[]     
mat2=[] 
dimonds=[]    
count=[]       
# print(mat1)
# print(mat2)
for i in range(a) :
    mat1.append([])
    mat2.append([]) #here
for i in range(a) :
    line = full[i+1]
    for j in range(len(line)) :
        if line[j]=="." or line[j] =="D" :
            mat2[i].append(1)
        else :
          mat2[i].append(line[j])
        mat1[i].append(line[j])

def traverse(mat1, row, col, source, mark) :
    #print(f"row{row} col{col} source{source} mark{mark} {mat1} ")
    if (row<0 or row>=a or col<0 or col>=b or mat1[row][col] == "#" or mat1[row][col] == mark) :
        return  
    if mat1[row][col] == "D":
        count.append("D")
#-------------------
    mat1[row][col] = mark   
    traverse(mat1,row+1,col,source,mark)  
    traverse(mat1,row-1,col,source,mark)  
    traverse(mat1,row,col+1,source,mark)  
    traverse(mat1,row,col-1,source,mark)  

def dfstraverse(mat1, row, col, mark):
    source = mat1[row][col]
    if source == mark :
        return
    traverse(mat1, row, col, source, mark)
#------------------------
mark = "x"   
for row in range(a) :
    for col in range(b) :
        if mat2[row][col] == 1 :
            dfstraverse(mat1, row, col, mark)
            dimonds.append(len(count))
            count=[]
print(max(dimonds),file=out)