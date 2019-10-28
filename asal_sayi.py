# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 14:39:20 2019

@author: hakik
"""

sonuc=[]
for n in range (2,100):
    for x in range (2,n):
        if n%x==0:
            break
    else:
        sonuc.append(n)
print(sonuc)    
    
#comment            
