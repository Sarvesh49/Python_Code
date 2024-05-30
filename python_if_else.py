'''CONTROL STATEMENT IN PYTHON
                        
                        CONTROL FLOW 
|------------------------------|--------------------------------------|
CONDITIONAL               TRANSFER                               ITERATIVE
STATEMENT                 STATEMENT                              STATEMENT
1. if                  1. break                                 1. for
2. if-elif             2. continue                              2. while
3. if-elif-else        3. pass

CONDITIONAL STATMENT

1 The if statement is used to test a specific condition.
If the condition is true, a block of code (if-block) will be executed.
An "if statement" is written by using the if keyword.

EXAMPLE:-
If statement:
a = 33
b = 200
if b > a:
  print("b is greater than a")

NESTED IF STATEMENT
You can have if statements inside if statements, this is called nested if statements.

EXAMPLE:-
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
    if x > 30:
      print("and also above 30!")

Elif

The elif keyword is Python's way of saying "if the previous conditions were not true, 
then try this condition".   
Example:- 

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

In this example a is equal to b, so the first condition is not true,
but the elif condition is true, so we print to screen that "a and b are equal".

Else

The else keyword catches anything which isn't caught by the preceding 
conditions.

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

In this example a is greater than b, so the first condition is not true, 
also the elif condition is not true, so we go to the else condition 
and print to screen that "a is greater than b".

You can also have an else without the elif:   
Example 
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

SHORT HAND IF...else
If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:
a = 2
b = 330
print("A") if a > b else print("B")

You can also have multiple else statements on the same line:
Example

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
--------------------------------------------------------------------------------------------------------
And
The and keyword is a logical operator, and is used to combine conditional statements:

Example
Test if a is greater than b, AND if c is greater than a:

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
------------------------------------------------------------------------------------------------
Or
The or keyword is a logical operator, and is used to combine conditional statements:

Example
Test if a is greater than b, OR if a is greater than c:

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
  ----------------------------------------------------------------------------------------------------------
Not
The not keyword is a logical operator, and is used to reverse the result of the conditional statement:

Example
Test if a is NOT greater than b:

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
------------------------------------------------------------------------------------------------------------------------------------------------------------
Ex 1:- Take english, math, science marks use if & else statements where marks less than 45 fail
Ex 2:- WAP for smallest of 2 numbers   use if & else statements
Ex 3:- wap for smallest of 4 numbers   use if & elif & else  statements 
Ex 4:- wap for smallest of 5 numbers   use if & elif & else  statements
Ex 5:- WAP for sum & Percentage of 3 subject marks and take gender if gender is femail take addmission otherwise addmission can not be taken
EX 6:- WAP for finding out number is even or odd 
EX 7:- WAP for finding number is +ve or -ve negative 
Ex 8:- WAP for finding out if person is old enough to vote
-----------------------------------------------------------------------------------------------------------------------------------------------------------

TRANSFER STATEMENT     
Loop control statements change execution from their normal sequence.
When execution leaves a scope, all automatic objects that were created in that scope are destroyed.
Python supports the following control or TRANSFER statements.

Break

Python break is used to terminate the execution of the loop. 
break statement in Python is used to bring the control out of the loop when some external condition is triggered. 
break statement is put inside the loop body (generally after if condition).  
It terminates the current loop, i.e., the loop in which it appears, 
and resumes execution at the next statement immediately after the end of that loop.
If the break statement is inside a nested loop, the break will terminate the innermost loop.
Python break statement Syntax:
Loop{
    Condition:
        break
    }

Ex:-
s = 'SarveshforSarvesh'
# Using for loop 
for letter in s: 
  
    print(letter) 
    # break the loop as soon it sees 'e' 
    # or 's' 
    if letter == 'e' or letter == 's': 
        break
  
print("Out of for loop"    ) 
print() 
  
i = 0
  
# Using while loop 
while True: 
    print(s[i]) 
  
    # break the loop as soon it sees 'e' 
    # or 's' 
    if s[i] == 'e' or s[i] == 's': 
        break
    i += 1
  
print("Out of while loop ")  

continue

Python Continue Statement returns the control to the beginning of the loop.
Python Continue statement is a loop control statement that forces to execute the next iteration of the loop
while skipping the rest of the code inside the loop for the current iteration only,
i.e. when the continue statement is executed in the loop, 
the code inside the loop following the continue statement will be skipped for the current iteration 
and the next iteration of the loop will begin.

Python continue Statement Syntax
while True:
    ...
    if x == 10:
        continue
    print(x)
Ex:- 
# Prints all letters except 'e' and 's' 
i = 0
a = 'aeiouaesauesau'
  
while i < len(a): 
    if a[i] == 'e' or a[i] == 's': 
        i += 1
        continue
          
    print('Current Letter :', a[i]) 
    i += 1
---------------------------------------------------------------------------------------------------------------------------------------
The Python pass statement is a null statement. 
But the difference between pass and comment is that comment is ignored by the interpreter whereas pass is not ignored.   
If we do not use pass or simply enter a comment or a blank here, we will receive an IndentationError error message.

Example:-
a = 10
b = 20
 
if(a<b):
  pass
else:
  print("b<a")