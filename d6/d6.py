#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  6 09:46:35 2025

@author: svenja
"""
import re
import neighbours as n

def d6_1():
    file=open("input.txt","r")
    problems=[]
    operator=[]
    result=0
    
    for line in file:
        line=line.strip("\n")
        line=re.split(" +",line)
        
                
        linenum=[int(x) for x in line if len(re.findall("^[0-9]+$", str(x)))>0 ] #get all numbers from lines
        if line!=[]: problems.append(linenum)
        
        operator=[s for s in line if len(re.findall("^[\*|\+]+$", str(s)))>0] #get all operators
        
    
    for i in range(len(problems[0])): #calculate numbers
        calculated=0
        calc=vertikal(problems,i)
        
        if operator[i]=="*":
            calculated+=1
            for num in calc:
                calculated*=num
        if operator[i]=="+":
            for num in calc:
                calculated+=num
        result+=calculated
                
    file.close()    
                
    return result



def d6_2():
    file=open("input.txt","r")
    problems=[]
    operator=[]
    result=0
    
    for line in file:
        
        if "*" in line:
            operator=line.split()
        
        line=re.sub(" ","0",line.strip("\n"))
        problems.append(line)
        
  
    pmaxlen=len(max(problems, key=len)) 
    problems=[x.ljust(pmaxlen," ") for x in problems] #get all problems to the sam elength, because spaces at the end are cut of
    vert=[vertikal(problems,i) for i in range(len(problems[0]))] #get vertikal numbers as lists

    calc=""
    for i in range(len(vert)):
        num=""
        
        for zif in vert[i]: num+=str(zif) #construk vertikal numbers from list
            
        if num!="0000": 
                calc+=(num.strip("0"))
                calc+="0"
        else: #if empty colums:separate at that position
                calc+=(",")
        
    
    calc=calc.split(",") 
    
    for j in range(len(calc)): #for each vertikal number: calculate with given operator
        calculated=0
        current=calc[j]
        if operator[j]=="*":
            calculated=1
            current=current.split("0")
            current.remove("")
            
            for num in current:
                num=int(num)
                calculated*=num
                
            
        if operator[j]=="+":
            current=current.split("0")
            current.remove("")
            
            for num in current:
                num=int(num)
                calculated+=num
                
        result+=calculated
        
    
    file.close()                   
    return result
   
    
    
def vertikal(l,startnum):
    
    rows=[l[0][startnum]]
    for i in range(len(l)-2):
        rows.append(n.bo(i,startnum,l)) #get bottom neighbour as while on exists
    return rows
        
        
        
    
print(d6_1())    
print(d6_2())

        