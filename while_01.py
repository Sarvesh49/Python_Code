'''Python Loops
Python has two primitive loop commands:

while loops
for loops

The while Loop
With the while loop we can execute a set of statements as long as a condition is true.
Python while loop is used when the number of iterations is unknown
While loop falls under the category of indefinite iteration.

Syntax of while loop in Python
while expression:
    statement(s)

Example
Print i as long as i is less than 6:
remember to increment i, or else the loop will continue forever.
i = 1
while i < 6:
  print(i)
  i += 1
The while loop requires relevant variables to be ready, 
in this example we need to define an indexing variable, i, which we set to 1.

With the break statement we can stop the loop even if the while condition is true:

Example
Exit the loop when i is 3:

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

With the continue statement we can stop the current iteration, and continue with the next:

Example
Continue to the next iteration if i is 3:

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

With the else statement we can run a block of code once when the condition no longer is true:

Example
Print a message once the condition is false:

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
------------------------------------------------------------------------------------------------------------
for loop in python

A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
This is less like the for keyword in other programming languages, 
and works more like an iterator method as found in other object-orientated programming languages.
With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
The for loop does not require an indexing variable to set beforehand.

Looping Through a String
Even strings are iterable objects, they contain a sequence of characters:

Example
Loop through the letters in the word "banana":

for x in "banana":
  print(x)

The range() Function
To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, 
starting from 0 by default, and increments by 1 (by default), and ends at a specified number.


Example
Using the range() function:

for x in range(6):
  print(x)

range(6) is not the values of 0 to 6, but the values 0 to 5.

The range() function defaults to 0 as a starting value, 
however it is possible to specify the starting value by adding a parameter: range(2, 6), 
which means values from 2 to 6 (but not including 6):

Example
Using the start parameter:

for x in range(2, 6):
  print(x)

The range() function defaults to increment the sequence by 1, 
however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):

Else in For Loop
The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

Example
Print all numbers from 0 to 5, and print a message when the loop has ended:

for x in range(6):
  print(x)
else:
  print("Finally finished!")
The else block will NOT be executed if the loop is stopped by a break statement.

Nested Loops
A nested loop is a loop inside a loop.

The "inner loop" will be executed one time for each iteration of the "outer loop":

Example
Print each adjective for every fruit:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

The pass Statement
for loops cannot be empty, but if you for some reason have a for loop with no content, 
put in the pass statement to avoid getting an error.

Example
for x in [0, 1, 2]:
  pass
--------------------------------------------------------------------------------------------------------------------------------------------------------
Patterns can be printed in python using simple for loops. 
First outer loop is used to handle the number of rows and the Inner nested loop is used to handle the number of columns. 
Manipulating the print statements, different number patterns, alphabet patterns, or star patterns can be printed. 
--------------------------------------------------------------------------------------------------------------------------------------------------------

Python * pyramid using for loop

# Simple Python program to print the Simple pyramid pattern   
n = int(input("Enter the number of rows"))       
# Here, we are declaring the integer variable to store the input rows  
# Here, we are declaring an outer loop to handle number of rows    
for i in range(0, n):    
    # Here, we are declaring an inner loop to handle number of columns    
    # Here, the values are changing according to outer loop    
        for j in range(0, i + 1):    
            # Here, we are declaring a for loop for printing stars    
            print("* ", end="")       
        # Here, we are giving the ending line after each row    
        print()  
--------------------------------------------------------------------------
In the above code, we have initialized the n variable to enter the number of rows for the pattern.
 We entered n = 5, the range of outer for loop will be 0 to 4.

The iteration of the inner for loop depends on the outer loop. 
The inner loop is responsible to print the number of columns.
In the first iteration, the value of i is 0, and it increased by 1, 
so it becomes 0+1, now inner loop iterated first time and print one star(*).
In the second iteration, the value of i is 1 and it increased by 1,
so it becomes 1+1, now inner loop iterated two times and print two-star (*).
The end argument prevents to jump into another line. 
It will printer the star until the loop is valid.
The last print statement is responsible for ending the line after each row.
---------------------------------------------------------------------------          
output
*
* *
* *  *
* *  *  *
* *  *  *  *
---------------------------------------------------------------------------------
using while loop
n=5
 
i=1;j=0
# while loop check the condition until the
# condition become false. if it is true then 
# enter in to loop and print the pattern
while(i<=n):
    while(j<=i-1):
        print("* ",end="") 
        j+=1
     # printing next line for each row
    print("\r") 
    j=0;i+=1
----------------------------------------------------------------------------------
Carriage return in Python
The carriage return character (\r) is a special control character that originated from the early days of typewriters
and teletype machines.
It represents the action of moving the cursor or print head back to the beginning of the current line. 
When encountered in a string or used in output operations.

The carriage return is represented by the escape sequence ‘\r ‘.
When the carriage return character is encountered in a string it moves the cursor to the beginning 
of the current line.

Syntax
print("--\r--")
----------------------------------------------------------------------------------
# Program to print full pyramid 
num_rows = int(input("Enter the number of rows"));
for i in range(0, num_rows):
  for j in range(0, num_rows-i-1):
    print(end=" ")
  for j in range(0, i+1):
    print("*", end=" ")
  print()
---------------------------------------------------------------------------------------------
Explnation:-
we will ask the user to input the number of rows that says 5, then using a variable I, 
the outer for loop iterates using the range function starting from 0, which ends with 5. 
Further, using variable j, the inner for loop iterates using the range function again to print spaces. 
Next, again, using the variable j, the innermost for loop for the printing of stars, 
and then control will go to the next line, the last step in the program, the print function. 
And this will work for i= 0 row, i=1 row, i=2 row, i= 3 rows, and i=4 row, and depending on these I values, 
the next two loops will be processed.
-------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------------
# Simple Python program to print the simple downward half - pyramid pattern    
rows = int(input("Enter the number of rows:"))   
# Here, we are declaring the integer variable to store the input rows   
# Here, we are declaring the outer for loop for executing in reversed order    
for i in range(rows + 1, 0, -1):      
    for j in range(0, i - 1):     # here, we are declaring the for loop to print the pattern  
        print("*", end=' ')    
    print(" ")    
Output:

Enter the number of rows: 5
* * * * *  
* * * *  
* * *  
* *  
*  
-----------------------------------------------------------------------------------------------------
Number Pattern
Code -

# Simple Python program to print the simple number pattern  
# Here, we are declaring the integer variable to store the input rows  
rows = int(input("Enter the number of rows: "))    
# Here, we are declaring the for loop that is used to print the number of rows    
for i in range(rows+1):    
# Here, we are declaring the for loop that is used to print the value of i after each iteration    
    for j in range(i):    
        print(i, end=" ")       # Here, we are printing the number in some pattern    
    # Here, this print is used for new line after each row to display pattern correctly    
    print(" ")    
Output:

Enter the number of rows: 5
1  
2 2  
3 3 3  
4 4 4 4  
5 5 5 5 5  
Explanation -

In the above code, we have printed the numbers according to rows value. 
The first row prints a single number. Next, two numbers, prints in the second row, 
and the next three number prints on the third row and so on. In the