#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 06:36:49 2025

@author: svenja
"""




#alle min abstände finden

def min_d(boxes):
    
    p=[]
    
    boxes1=[z for z in boxes]
    
    for k in range(10):
        mind=100000000
        mem=[]
        
        
        if k%10==0:
            print("#",end='')
        
        for i in range(len(boxes)):
            
            
            box0=[int(x) for x in boxes[i]]
            for j in range(len(boxes1)):
                
                
                box1=[int(y) for y in boxes1[j]]
                if box1!=box0 and [box1,box0] not in p:
                    
                    d=(int(box0[0]-box1[0])**2+int(box0[1]-box1[1])**2+int(box0[2]-box1[2])**2)
                    if mind>d:
                        mind=d
                        mem=[box0,box1]
        
   # print(mem)
        if len(mem)>0:
            rem=[str(s) for s in mem[1]]
            if rem in boxes1:
               boxes1.remove(rem)
               
        
        
        p.append(mem)
            
           
             
    return p



def merge(num):
    mer=num
    merged=[x for x in num]
  #  mem=[]
    
  
    #for k in range(10):
    for i in range(len(merged)):
            #merge
            for j in range(len(mer)):
              #  if i!=j:
                    if merged[i][0]==mer[j][0]:
                        if mer[j][1] not in merged[i]:
                            merged[i].insert(0,mer[j][1])
                        
                    if merged[i][0]==mer[j][1]:
                        
                        if mer[j][0] not in merged[i]:
                            merged[i].insert(0,mer[j][0])
                            
                    if merged[i][len(merged[i])-1]==mer[j][0]:
                        if mer[j][0] not in merged[i]:
                            merged[i].insert(0,mer[j][0])
                        
                    if merged[i][len(merged[i])-1]==mer[j][len(mer[j])-1]:
                        
                        if mer[j][1] not in merged[i]:
                            merged[i].insert(0,mer[j][1])
         
        
        
    return merged
  
                    
            
            
            
    


            

file=open("input.txt","r")

boxes=[]

for line in file:
    line=line.strip("\n")
    box=line.split(",")
    boxes.append(box)

circuits=[] 


#print(min_d(boxes))   
m=min_d(boxes)

for i in range(len(m)):
    m[i]=[str(x[0])+str(x[1])+str(x[2]) for x in m[i]]


#m[1]=[str(x[0])+str(x[1])+str(x[2]) for x in m[1]]

#n=merge(merge(m))

#print(merge(m))

    

#merge(m)

        
    
print(m)
    


