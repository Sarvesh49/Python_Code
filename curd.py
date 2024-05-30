'''#import calculations
print(calculations.y)

print(calculations.remainder(100,40))

a1=calculations.add
x=a1(18,21)
print(x)


from calculations import add

a=int(input("enter the number :"))
b=int(input("enter the number :"))
print(add(a,b))

import calculations as cal
a=int(input("enter the number"))
b=int(input("enter the number"))
print(cal.multi(a,b))

from calculations import y,add,remainder

print(y)
print(remainder(3,4)) 
print(add(5,6))

from calculations import *

print(y)
print(multi(4,5))

import calculations
print(dir(calculations))

'''