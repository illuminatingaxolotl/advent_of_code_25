#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 08:58:27 2025

@author: svenja
"""
import neighbours as n

def d7_1(*show_map):
    file=open("input.txt","r")
    map0=[]
    scount=0
    
    #put input in list
    for line in file:
        line.strip("\n")
        a=[]
        for element in line:
            a.append(element)
        map0.append(a)
        
    for i in range(len(map0)):
        if "S" in map0[i]: #put first | below S 
            s_index=map0[0].index("S")
            n0,n1=n.in_bo(0,s_index,map0)

            if n.in_bo(0,s_index,map0)!=None:
                map0[n0][n1]="|"
        
                
        if "^" in map0[i]:
            c=map0[i].count("^")
            
            for j in range(c): #for all ^ in one line:split into two | 
                v_index=map0[i].index("^")
                n10,n11=n.in_le(i,v_index,map0)
                n20,n21=n.in_ri(i,v_index,map0)
                ntop0,ntop1=n.in_to(i,v_index,map0)
            

                if map0[ntop0][ntop1]=="|":
                    scount+=1 #split count +1
                    if n.in_le(i,v_index,map0)!=None:
                            map0[n10][n11]="|"
       
                        
                    if n.in_bo(i,v_index,map0)!=None:
                                map0[n20][n21]="|"
                map0[i][v_index]="0" #if ^ split |: turn ^ to 0
                                
            
        for l in range(len(map0[i])):
                
            if map0[i][l]!="^" and  map0[i][l]!="0": #continue all | to next level
                if n.in_to(i,l,map0)!=None:
                    ntop0,ntop1=n.in_to(i,l,map0)
            
                    if map0[ntop0][ntop1]=="|":
                        map0[i][l]="|"
                            
    if True in show_map: #show map                 
        for line in map0:
            s=""
            for element in line:
                if element=="0":
                    element="^"
                s+=element
            print(s)
    return scount
       


def d7_2(*show_map):
    
    file=open("input.txt","r")
    map0=[]
    
    
    #put input in two dimensional list
    i=0
    for line in file:
        i+=1
        if i%2==1:
            line.strip("\n")
            a=[]
            for element in line:
               
                if element=="S":
                    element=1
                if element==".":
                    element=0
                if element!="\n":
                    a.append(element)
            map0.append(a)
            
            
    for i in range(1,len(map0)):
        for j in range(1,len(map0[i])):
            if map0[i][j]=="^":
                n0=n.to(i,j,map0) #top neighbour of ^
                n1in=n.in_le(i,j,map0) #get left and right neighbour of ^
                n2in=n.in_ri(i,j,map0) 
          
            
                if  map0[n1in[0]][n1in[1]]!="^" and map0[n2in[0]][n2in[1]]!="^": #if neighbours are not ^: add top neighbour
                    map0[n1in[0]][n1in[1]]+=n0
                    map0[n2in[0]][n2in[1]]+=n0
                    
            else: #if element isn#t ^: if top neighbour isn#t n add to element
                n0=n.to(i,j,map0)
                if n0!="^":
                    map0[i][j]+=n0
      

    res=0

    for num in (map0[len(map0)-1]): #add all numbers in last column together
        if num!="^":
            res+=num
            
            
    if True in show_map: #show map
        for line in map0:
                s=""
                
                for element in line:
      
                    if element==0 or isinstance(element,int):
                       element=(". ")
                    
                    if len(str(element))<2:
                        s+=str(element)+" "
                    else:s+=str(element)
               
                s+="\n"
                for element in line:
                    
                    if element==0 or element=="^":
                       element=(". ")
                    
                    if len(str(element))<2:
                        s+=str(element)+" "
                    else:s+=str(element)

                print(s)
    return res



print(d7_1(True))
print(d7_2(True))

    
