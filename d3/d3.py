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
    
   
    for bank in file:
        
        
        bank=bank.strip("\n")
        bank=[int(x) for x in bank]
        
        
        start=len(bank)-13
        current=bank[start]
        
        mem=0
        mincount=0
       
        
        for i in range(start+1):

            mincount+=1
            comp=bank[start-i]
            compid=start-i

            if comp>=current:
                current=comp
                
                for i in range(mincount):
 
                    min0=min(bank[compid:])
                    minindex=bank[compid:].index(min0)+compid
                    bank.pop(minindex)
                   
       
                mincount=0
                mem=compid

        bank=(bank[mem:])
        print(bank)

        joltage_line=""
        
        for num in bank:
            joltage_line+=str(num)
 
        
        joltage+=int(joltage_line)

    file.close()
    return joltage
        
        
              

print(d3_2())