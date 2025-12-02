#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 07:50:50 2025

@author: svenja
"""

def d2_1(): #this could have been done so much easier, why did i do it like that??
    idrange="12077-25471,4343258-4520548,53-81,43661-93348,6077-11830,2121124544-2121279534,631383-666113,5204516-5270916,411268-591930,783-1147,7575717634-7575795422,8613757494-8613800013,4-19,573518173-573624458,134794-312366,18345305-18402485,109442-132958,59361146-59451093,1171-2793,736409-927243,27424-41933,93-216,22119318-22282041,2854-4778,318142-398442,9477235089-9477417488,679497-734823,28-49,968753-1053291,267179606-267355722,326-780,1533294120-1533349219"
    idrange=idrange.split(",")
    invalid=[]
    
    
    
    for element in idrange:
        element=element.split("-")
        start=int(element[0])
        end=int(element[1])+1
        
        #all ids in range
        ids=[x for x in range(start,end)]
        
        
        #get divisors of length of id
        for singleid in ids:
            singleid=str(singleid)
            idlen=len(singleid)
            divisors=getdivisors(idlen)
            
            
            #only divisors who are themselves divisible by 2 are able to produce parts that are divisible by 2
            for divisor in divisors:
                if (len(singleid)/divisor)%2==1:
                    divisors.remove(divisor)
            #print(singleid, divisors, idlen)
            
            
            
            for divisor in divisors:
                #print(divisor)
                splitid=[]
                
                
                # for each divisor: split singleid into as many substrings, as the divisor says
                parts=divisor
                while parts<idlen+1:
                    splitid.append(singleid[(parts-divisor):parts])
                    parts=parts+divisor
    
            
                # if all those substrings are the same: add them to invalid list (if id isn#t already in the list)
                if all(subids == splitid[0] for subids in splitid) and not(int(singleid) in invalid) and int(len(singleid))%2==0: #if len(singleid)%2==0: id can#t consist of two of the same parts, because not devidible by 2
                    invalid.append(int(singleid))
                    
                
    
    
    return(sum(invalid))
                #print(splitid)
                
def d2_2():
    idrange="12077-25471,4343258-4520548,53-81,43661-93348,6077-11830,2121124544-2121279534,631383-666113,5204516-5270916,411268-591930,783-1147,7575717634-7575795422,8613757494-8613800013,4-19,573518173-573624458,134794-312366,18345305-18402485,109442-132958,59361146-59451093,1171-2793,736409-927243,27424-41933,93-216,22119318-22282041,2854-4778,318142-398442,9477235089-9477417488,679497-734823,28-49,968753-1053291,267179606-267355722,326-780,1533294120-1533349219"
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
                
            
            
        
       # print(ids)
        
        
        #print(start,end)
    
   #print(ids)
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