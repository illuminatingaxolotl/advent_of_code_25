#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 06:38:51 2025

@author: svenja
"""

import neighbours as n

def d4_1():
    result=0
    file=open("input.txt","r")
    map0=[]
    for line in file:
        line=line.strip("\n")
        map0.append(line)
        
    for i in range(len(map0)):
        for j in range(len(map0[i])):
            if map0[i][j]=="@":
                  
                neighbours=n.al(i,j,map0)
                scrollcount=neighbours.count("@")
                
                if scrollcount<4:
                    result+=1
    return result
                       
def d4_2():
    
    
    result=0
    file=open("input.txt","r")
    map0=[]
    durchgang=0
    for line in file:
            #print(line)
            line=line.strip("\n")
            roh=line
            line=[]
            for char in roh:
                line.append(char)
                
            map0.append(line)
   
    
    for k in range(1000):

        for i in range(len(map0)):
            if durchgang>len(map0)*len(map0[i]): break
            for j in range(len(map0[i])):
                    if map0[i][j]=="@":
                          
                        neighbours=n.al(i,j,map0)
                        scrollcount=neighbours.count("@")
                        
                        if scrollcount<4:
                            result+=1
                            map0[i][j]="."
                        else:
                            durchgang+=1
                        
    return result
                    
                 
print(d4_1())
print(d4_2())