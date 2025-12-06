#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 09:45:12 2025

@author: svenja
"""



def d1_1():
    wpos=50 #position of wheel
    file=open("input1.txt","r")
    zcount=0 #counts how often wheel reaches zero
    for line in file:
        line.strip("\n")
        
        direction=line[0]
        num=int(line[1:]) 
        
        #turn wheel
        if direction=="R":
            wpos=(wpos+num)%100
            
        if direction=="L":
            wpos=(wpos-num)%100
        #count how often zero is reached after turning
        if wpos==0:zcount+=1

    return zcount
    file.close()
    
    
    
def d1_2():
    wpos=50 #position of wheel
    file=open("input1.txt","r")
    zcount=0 #counts how often wheel reaches zero
    for line in file:
        line.strip("\n")
        
        direction=line[0]
        num=int(line[1:])
        
        if num>=100:
            zcount+=int(num/100) #hunderter in num: so oft kommt wheel auf jeden fall an null vorbei
            num=(num-(int(num/100)*100))#zehner in num

        
        if direction=="R":
           wpos=(wpos+num)%100 
           
           if (wpos-num)<0 or wpos==0: # kommt wheel nach den hunderten drehungen noch mal an null vorbei?
                zcount+=1
  
            
        if direction=="L":
            wpos=(wpos-num)%100
            
            if wpos+num>100 or wpos==0: # kommt wheel nach den hunderten drehungen noch mal an null vorbei?
                zcount+=1
     

    return zcount
    file.close()
    
    
print(d1_1())
print(d1_2())