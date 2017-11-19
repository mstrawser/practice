# -*- coding: utf-8 -*-
"""
Created on 11/18/2017

@author: mstrawser
"""
x = int(input('Enter an interger: '))

if x%2 == 0:
    
    if x%3 == 0:
        
        print('Divisible by 2 and 3')
 
    else:
        
        print('Divisible by 2 and not by 3')
        
elif x%3 == 0:
    print('Divisible by 3 and not by 2')

else:
    print('Divisible by neither 2 nor 3')
