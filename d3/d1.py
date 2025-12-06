# -*- coding: utf-8 -*-
"""
Spyder-Editor

Dies ist eine temporäre Skriptdatei.
"""

def d3_1():
    joltage=0
    file=open("input.txt","r")
   
    for bank in file:
        bank=bank.strip("\n")
        bank=[int(x) for x in bank]
        max0=max(bank)
        maxindex=bank.index(max0)
       
        if maxindex==len(bank)-1:
            max1=max0
            bank.remove(max0)
            max0=max(bank)
            
        else:
            max1=max(bank[(maxindex+1):])

        num=int(str(max0)+str(max1))
        joltage+=num
    
    file.close()
    return joltage


def d3_2(): 
    joltage=0
    file=open("input.txt","r")
    res2=[]
   
    for bank in file:
        bank=bank.strip("\n")
        bank=[int(x) for x in bank]
        print(bank)
        
        remove=len(bank)-12
        res2.append(0)
       # print(remove)
       
        res=[]
        
        
        i=0
        while len(res)<13:
            window0=i
            window1=i+remove
            
            m=max(bank[window0:window1])
            
            ind=((bank[window0:window1]).index(m))+i
            #print(ind)
            
            res.append([ind,m])
            bank[ind]=0
            
            
            
            i+=1
            
        
            
        print(res)
    
           
          
            

print(d3_2())