#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 07:04:43 2025

@author: svenja

"""

def d5_1():
    file_r=open("input_range.txt","r")
    file_s=open("input_singular.txt","r")
    f_count=0
    ids=[]
    
    for num in file_s:
            num=int(num.strip("\n"))
            ids.append(num) #all ids we have to check
            
    
    for line in file_r: #go through all ranges
        line=line.strip("\n")
        line=line.split("-")
        line=[int(x) for x in line]
        
        for num in ids:
            if num >= line[0] and num <= line[1]: #for each id in ids: check if it is in range
                f_count+=1 #when it is: count it as fresh ingredient
                ids=[x for x in ids if x!=num] #if it is:remove from list, so it does#nt count double, if in multiple ranges
                
                
    return f_count

def d5_2():
    file_r=open("input_range.txt","r")
    ids=[]
    checkedids=[]
    
    for line in file_r:
        line=line.strip("\n")
        line=line.split("-")
        line=[int(x) for x in line]
        ids.append(line) #save all ranges 
        
    ids.sort() #sort ranges by first element
   
    for element in ids:
        check=0
        for i in range(len(checkedids)):
            cids=checkedids[i]
           
            if inrange(cids,element[0]) and inrange(cids,element[1]): #if current range is included in a range,that already exists: do nothing
                check=1
                break
            
            #if current range is partly included in an already existing range: add those two ranges together to one larger range
            if element[0]<cids[0] and inrange(cids,element[1]): 
                checkedids[i][0]=element[0]
                check=1
                break
                
            if element[1]>cids[1] and inrange(cids,element[0]):
                checkedids[i][1]=element[1]
                check=1
                break
                
        #if range doesn#t exist at all at this point: append it
        if check==0:
            checkedids.append(element)
                

    result=0
    for ranges in checkedids: #count all the elements in the different ranges and add them
        result+=((ranges[1]+1)-ranges[0])
        
    return result
    
        
    

def inrange(range0,num): #check if number num is located in range between range0[0] and range0[1]
    if range0[0]<=num<=range0[1]:
        return True
    else:
        return False
    
        
print(d5_1())
print(d5_2())