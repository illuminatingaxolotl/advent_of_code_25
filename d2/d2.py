#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 07:50:50 2025

@author: svenja
"""

def d2_1(): 
    idrange="11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    idrange=idrange.split(",")
    invalid=[]


    for element in idrange:
        element=element.split("-")
        start=int(element[0])
        end=int(element[1])+1
        
        #all ids in range
        ids=[x for x in range(start,end)]
 
        for singleid in ids:
            
            singleid=str(singleid)
            idlen=len(singleid)
            
            if idlen%2==0:
            
               #if id is divisible by 2 check if first and last part of id are the same
               splitid1=singleid[0:int(idlen/2)]
               splitid2=singleid[int(idlen/2):]
      
                
               if splitid1==splitid2 and not(int(singleid) in invalid):
                    invalid.append(int(singleid)) #if it is the same, it#s invalid
                    
    return(sum(invalid))
        
                
def d2_2():
    idrange="11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-212121212411-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    idrange=idrange.split(",")
    invalid=[]
    
    
    
    for element in idrange:
        element=element.split("-")
        start=int(element[0])
        end=int(element[1])+1
        
        #all ids in range
        ids=[x for x in range(start,end)]
        
        
        
        for singleid in ids:
            singleid=str(singleid)
            idlen=len(singleid)
            divisors=getdivisors(idlen) #get divisors of length of id
        
            for divisor in divisors:
                splitid=[]
                
                # for each divisor: split singleid into as many substrings, as the divisor says
                parts=divisor
                while parts<idlen+1:
                    splitid.append(singleid[(parts-divisor):parts])
                    parts=parts+divisor
    
                    
                # if all those substrings are the same: add them to invalid list (if id isn#t already in the list)
                if all(subids == splitid[0] for subids in splitid) and not(int(singleid) in invalid):
                    invalid.append(int(singleid))
                    
                
    
    
    return(sum(invalid))
                
            

def getdivisors(num):
    divisors=[]
    for i in range(1,num):
        if num%i == 0 :
            divisors.append(i)
            
    return divisors

def getsum(l):
    c=0
    for element in l:
        c+=element
    return c
                

print(d2_1())
print(d2_2())