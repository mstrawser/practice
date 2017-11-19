
"""
Created on 11/18/2017

@author: mstrawser
"""
for w in range(100):
    x = w + 1
    fizz = x % 3 == 0
    buzz = x % 5 == 0
    
if fizz:
    if buzz:
        print('FizzBuzz')
    else: 
        print('Fizz')
elif buzz:
    print('Buzz')
else:
    print (x)
