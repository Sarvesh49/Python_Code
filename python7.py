# Python Operators
''' Operators are used to perform operations on variables and values.
Python divides the operators in the following groups:
------------------------------------------------------------------------------------------------
1 Arithmetic operators
Arithmetic operators are used with numeric values to perform common mathematical operations: 
+,-,/,*,%,**,//
%--- returns  modulus or remainder  | **---- returns exp
-------------------------------------------------------------------------------------------------
2 Assignment operators
Assignment operators are used to assign values to variables:
= ------>	x = 5	x = 5	
+=------>	x += 3	x = x + 3	
-=------>	x -= 3	x = x - 3	
*=	------> x *= 3	x = x * 3	
/=	------> x /= 3	x = x / 3	
%=	------> x %= 3	x = x % 3	
//=	------> x //= 3	x = x // 3	
**=------>	x **= 3	x = x ** 3	
&=	------> x &= 3	x = x & 3	
|=	------> x |= 3	x = x | 3	
^=	------> x ^= 3	x = x ^ 3	
>>=	------> x >>= 3	x = x >> 3	
<<=	------> x <<= 3	x = x << 3
3 Comparison operators
==	Equal--------------->	        x == y	
!=	Not equal--------------->       x != y	
>	Greater than--------------->	x > y	
<	Less than--------------->	    x < y	
>=	Greater than or equal to--------------->	x >= y	
<=	Less than or equal to--------------->	    x <= y
4 Logical operators
and 	Returns True if both statements are true------->	x < 5 and  x < 10	
or	    Returns True if one of the statements is true------>	x < 5 or x < 4	
not  	Reverse the result,
        returns False if the result is true-------->  	not(x < 5 and x < 10)
5 Identity operators
is --------> 	Returns True if both variables are the same object--------> 	x is y	
is not --------> Returns True if both variables are not the same object--------> x is not y
6 Membership operators
in --------> 	Returns True if a sequence with the specified value is present in the object	x in y	
not in -------->	Returns True if a sequence with the specified value is not present in the object	x not in y
7 Bitwise operators
&--------> 	AND	Sets each bit to 1 if both bits are 1-------->	x & y	
|-------->	OR	Sets each bit to 1 if one of two bits is 1-------->	x | y	
^	-------->XOR	Sets each bit to 1 if only one of two bits is 1-------->	x ^ y	
~	-------->NOT	Inverts all the bits-------->	~x	
<<	-------->Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off-------->	x << 2	
>>	-------->Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >>2
---------------------------------------------------------------------------------------------------------------------------------------------------------
EXAMPLE1 :- ARITHEMETIC OPERATOR
a = 32    # Initialize the value of a  
b = 6      # Initialize the value of b  
print('Addition of two numbers:',a+b)  
print('Subtraction of two numbers:',a-b)  
print('Multiplication of two numbers:',a*b)  
print('Division of two numbers:',a/b)  
print('Reminder of two numbers:',a%b)  
print('Exponent of two numbers:',a**b)  
print('Floor division of two numbers:',a//b)
---------------------------------------------------------------------------------------------------------------------------------
EXAMPLE2 :- Comparison operator

a = 32      # Initialize the value of a  
b = 6       # Initialize the value of b  
print('Two numbers are equal or not:',a==b)  
print('Two numbers are not equal or not:',a!=b)  
print('a is less than or equal to b:',a<=b)  
print('a is greater than or equal to b:',a>=b)  
print('a is greater b:',a>b)  
print('a is less than b:',a<b)  
------------------------------------------------------------------------------------------------------------------
EXAMPLE3:- Assignment Operators

a = 32         # Initialize the value of a  
b = 6          # Initialize the value of b  
print('a=b:', a==b)  
print('a+=b:', a+b)  
print('a-=b:', a-b)  
print('a*=b:', a*b)  
print('a%=b:', a%b)  
print('a**=b:', a**b)  
print('a//=b:', a//b) 
------------------------------------------------------------------------------------------------------------------
EXAMPLE 4:- LOGICAL OPERATORS

a = 5          # initialize the value of a          
print(Is this statement true?:',a > 3 and a < 5)  
print('Any one statement is true?:',a > 3 or a < 5)  
print('Each statement is true then return False and vice-versa:',(not(a > 3 and a < 5)))   
------------------------------------------------------------------------------------------------------------------
EXAMPLE 5 :- Membership Operators

x = ["Rose", "Lotus"]  
print(' Is value Present?', "Rose" in x)  
print(' Is value not Present?', "Riya" not in x)  

-----------------------------------------------------------------------------------------------------------------
EXAMPLE 6:- Identity Operators
a = ["Rose", "Lotus"]  
b = ["Rose", "Lotus"]  
c = a  
print(a is c)  
print(a is not c)  
print(a is b)  
print(a is not b)  
print(a == b)  
print(a != b) 
----------------------------------------------------------------------------------------------------------------
EXAMPLE 7:-  Bitwise operators

a = 5          # initialize the value of a  
b = 6          # initialize the value of b  
print('a&b:', a&b)  
print('a|b:', a|b)  
print('a^b:', a^b)  
print('~a:', ~a)  
print('a<<b:', a<<b)  
print('a>>b:', a>>b)  


Examples for partcise 
1 take user input of 2 numbers and Perform addtion on this numbers
2 take user input of 2 numbers and Perform subtraction on this numbers
3 take user input of 2 numbers and Perform division on this numbers
4 take user input of 2 numbers and Perform modulus on this numbers
5 take user input of 2 numbers and perform exponential on this numbers