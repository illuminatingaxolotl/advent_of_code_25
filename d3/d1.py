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
        maxindex=bank.bank(max0)
       
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


def d3_2(): #funktioniert nicht
    file=open("input.txt","r")
    result=0
    
    for line in file:
        neudrei=len(line)-13
        line=line.strip("\n")
        line=[int(x) for x in line]
        
        
        front=line[:(neudrei+1)]
        
        
        
        maxfrontin=front.index(max(front))
        remcount=0
        for i in range(len(front)):
            
           
                linewithountfront=line[maxfrontin:]
           
                remcount=len(line)-len(linewithountfront)
                #print(remcount)
                while remcount<neudrei:
                    linewithountfront.remove(min(linewithountfront))
                    remcount+=1
        #print(linewithountfront)
                    
        joltage=""
        
        
        for element in linewithountfront:
            joltage+=str(element)
        joltage=int(joltage)
        result+=joltage#
    file.close()
    return result
            

def d3_2_neu(): #funktioniert nicht
    file=open("input.txt","r")
    
    
    for line in file:
        
        
        
        line=line.strip("\n")
        line=[int(x) for x in line]
        
        revline=[]
        for i in range(len(line)):
            revline.append(line[len(line)-i-1])
        
        
        
        c9=line.count(9)
        c8=line.count(8)
        c7=line.count(7)
        c6=line.count(6)
        c5=line.count(5)
        c4=line.count(4)
        c3=line.count(3)
        c2=line.count(2)
        c1=line.count(1)
        voltage=[]
        for element in line:
            voltage.append(0)
            
        c=0
        
        revline,line=line,revline
        
        
        
        for i in range(c9):
                if c>11:break
                ind=line.index(9)
                
                voltage[ind]=line[ind]
                line[ind]=0
                
                c+=1
                
           
        for i in range(c8):
                if c>11:break
                ind=line.index(8)
                voltage[ind]=line[ind]
                line[ind]=0
                c+=1
                
        for i in range(c7):
                if c>11:break
                ind=line.index(7)
                voltage[ind]=line[ind]
                line[ind]=0
                c+=1
                
        for i in range(c6):
                if c>11:break
                ind=line.index(6)
                voltage[ind]=line[ind]
                line[ind]=0
                c+=1
                
        for i in range(c5):
                if c>11:break
                ind=line.index(5)
                voltage[ind]=line[ind]
                line[ind]=0
                c+=1
                
        for i in range(c4):
                if c>11:break
                ind=line.index(4)
                voltage[ind]=line[ind]
                line[ind]=0
                c+=1
                
                
        for i in range(c3):
                if c>11:break
                ind=line.index(3)
                voltage[ind]=line[ind]
                line[ind]=0
                c+=1
                
        for i in range(c2):
                if c>11:break
                ind=line.index(2)
                voltage[ind]=line[ind]
                line[ind]=0
                c+=1
                
        for i in range(c1):
                if c>11:break
                ind=line.index(1)
                voltage[ind]=line[ind]
                line[ind]=0
                c+=1
                
 
        print(voltage)
            

print(d3_1())