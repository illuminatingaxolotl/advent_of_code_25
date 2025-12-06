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
        #print(bank)
        #memory=[0 for x in bank]
        
        
        
        start=len(bank)-13
        #print(start)
        current=bank[start]
        currentid=start
        mem=0
        
        print()
        
        mincount=0
        for i in range(start+1):
            #print(start-i)
            mincount+=1
            comp=bank[start-i]
            compid=start-i
            #print(comp)
            
            
            if comp>=current:
                current=comp
                
                for i in range(mincount):
                    #print(bank[compid:])
                    min0=min(bank[compid:])
                   # print(min0)
                    minindex=bank[compid:].index(min0)+compid
                   # print(minindex)
                    bank.pop(minindex)
                   # print(bank[compid:])
       
                mincount=0
                #print(compid)
                
                mem=compid
        
        
       # print(mem)
      
       
      #print(bank)
        bank=(bank[mem:])
        print(bank)
        #print(bank[compid:])
        # while len(bank)>12:
        #     bank.remove(min(bank))
        
        
        
        joltage_line=""
        
        for num in bank:
            joltage_line+=str(num)
            
        #print(joltage_line)
            
      
        joltage+=int(joltage_line)
    
            
        

    
    file.close()
    return joltage
        
        
              
        


def getmax(l,memory):
        
        if len(l)==1:
            return memory+str(l[0])
        
        else:
            maxpos=l.index(max(l))
            l[maxpos]=0
            return getmax(l[maxpos:],memory)
        
        #return memory
        
        
           
          
            

print(d3_2())