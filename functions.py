 '''        Python Functions
A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.

Creating a Function
In Python a function is defined using the def keyword:

Example 1
def my_function():
  print("Hello from a function")

Calling a Function
To call a function, use the function name followed by parenthesis:

Example 2
def my_function():
  print("Hello from a function")

my_function()
----------------------------------------------------------------------------------------------------------------
 #  Arguments
Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. 
You can add as many arguments as you want,
just separate them with a comma.

The following example has a function with one argument (fname).
When the function is called, we pass along a first name,
which is used inside the function to print the full name:

Example 2
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
Arguments are often shortened to args in Python documentations.
---------------------------------------------------------------------------------------------------------------

Parameters or Arguments?
The terms parameter and argument can be used for the same thing: information that are passed into a function.

From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the value that is sent to the function when it is called.

# Number of Arguments
By default, a function must be called with the correct number of arguments.
Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments,
 not more, and not less.

Example 3
This function expects 2 arguments, and gets 2 arguments:

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
If you try to call the function with 1 or 3 arguments, you will get an error:
Example
This function expects 2 arguments, but gets only 1:

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil")
--------------------------------------------------------------------------------------------------------------------
Arbitrary Arguments, *args
If you do not know how many arguments that will be passed into your function, 
add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:

Example 1
If the number of arguments is unknown, add a * before the parameter name:

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

Arbitrary Arguments are often shortened to *args in Python documentations.
---------------------------------------------------------------------------------------------------------------
Keyword Arguments
You can also send arguments with the key = value syntax.

This way the order of the arguments does not matter.

Example 1
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
---------------------------------------------------------------------------------------------------------------
The phrase Keyword Arguments are often shortened to kwargs in Python documentations.

Arbitrary Keyword Arguments, **kwargs
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: 
** before the parameter name in the function definition.

This way the function will receive a dictionary of arguments, and can access the items accordingly:

Example
If the number of keyword arguments is unknown, add a double ** before the parameter name:

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

Arbitrary Kword Arguments are often shortened to **kwargs in Python documentations.
--------------------------------------------------------------------------------------------
Default Parameter Value
The following example shows how to use a default parameter value.

If we call the function without argument, it uses the default value:

Example 1
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
-----------------------------------------------------------------------------------------------
You can send any data types of argument to a function (string, number, list, dictionary etc.), 
and it will be treated as the same data type inside the function.

E.g. if you send a List as an argument, it will still be a List when it reaches the function:

Example 1
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
-----------------------------------------------------------------------------------
Return Values
To let a function return a value, use the return statement:

Example 1
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

The pass Statement
function definitions cannot be empty, but if you for some reason have a function definition with no content,
put in the pass statement to avoid getting an error.

Example 1
def myfunction():
  pass
-----------------------------------------------------------------------------------------------------  
Positional-Only Arguments

You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.

To specify that a function can have only positional arguments, add , / after the arguments:

Example
def my_function(x, /):
  print(x)

my_function(3)
Without the , / you are actually allowed to use keyword arguments 
even if the function expects positional arguments:

Example 2
def my_function(x):
  print(x)

my_function(x = 3)
But when adding the , / you will get an error if you try to send a keyword argument:

Example 3
def my_function(x, /):
  print(x)

my_function(x = 3)

Keyword-Only Arguments
To specify that a function can have only keyword arguments, add *, before the arguments:

Example 4
def my_function(*, x):
  print(x)

my_function(x = 3)
Without the *, you are allowed to use positionale arguments even if the function expects keyword arguments:

Example 4
def my_function(x):
  print(x)

my_function(3)
But when adding the *, / you will get an error if you try to send a positional argument:

Example
def my_function(*, x):
  print(x)

my_function(3)
-----------------------------------------------------------------------------------------------
Combine Positional-Only and Keyword-Only
You can combine the two argument types in the same function.

Any argument before the / , are positional-only, and any argument after the *, are keyword-only.

Example 1
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)
----------------------------------------------------------------------------------------------------------------
# Recursion

Python also accepts function recursion, which means a defined function can call itself.

Recursion is a common mathematical and programming concept. It means that a function calls itself. 
This has the benefit of meaning that you can loop through data to reach a result.

The developer should be very careful with recursion as it can be quite easy to slip into writing a function 
which never terminates, or one that uses excess amounts of memory or processor power.
However, when written correctly recursion can be a very efficient and 
mathematically-elegant approach to programming.

In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). 
We use the k variable as the data, which decrements (-1) every time we recurse. 
The recursion ends when the condition is not greater than 0 (i.e. when it is 0).

To a new developer it can take some time to work out how exactly this works,
best way to find out is by testing and modifying it.

Example 1
Recursion Example

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

examples for Practise

1 create function for addtion and substraction 
2 create function for Person and take age,gender and education AND CALL THE Function
3 create a function to find sqaure of the number
------------------------------------------------------------------------------------------------------------------
Python Lambda

A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.

Syntax :-
lambda arguments : expression
The expression is executed and the result is returned:

Example 1
Add 10 to argument a, and return the result:

x = lambda a : a + 10
print(x(5))

Lambda functions can take any number of arguments:

Example 2
Multiply argument a with argument b and return the result:

x = lambda a, b : a * b
print(x(5, 6))
Example
Summarize argument a, b, and c and return the result:

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

-----------------------------------------------------------------------------------------------------------
Why Use Lambda Functions?

The power of lambda is better shown when you use them as an anonymous function inside another function.

Say you have a function definition that takes one argument, 
and that argument will be multiplied with an unknown number:

def myfunc(n):
  return lambda a : a * n
Use that function definition to make a function that always doubles the number you send in:

Example 1
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
Or, use the same function definition to make a function that always triples the number you send in:

Examplec1
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))
Or, use the same function definition to make both functions, in the same program:

Example 2
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
note: -
Use lambda functions when an anonymous function is required for a short period of time.
---------------------------------------------------------------------------------------------------------------------------

Types of variables

There are two types of variables

1 global variables
2 local variables

1) global variables
The variable which is declared outside the function are called as global variables 
and there that are accessible through out the program
These are those which are defined outside any function and which are accessible throughout the program,
i.e., inside and outside of every function. Let’s see how to create a Python global variable.

Ex 1
# This function uses global variable s
def f():
  print("Inside Function", s)

# Global scope
s = "I love my India"
f()
print("Outside Function", s)

The variable s is defined as the global variable and is used both inside the function as well as outside the function.

Note: As there are no locals, the value from the globals will be used but make sure both the local 
and the global variables should have same name.
--------------------------------------------------------------------------------------------------------------------
Why do we use Local and Global variables in Python?

Now, what if there is a Python variable with the same name initialized inside a function as well as globally? 
Now the question arises, will the local variable will have some effect on the global variable or vice versa, 
and what will happen if we change the value of a variable inside of the function f()? 
Will it affect the globals as well? We test it in the following piece of code:
Example:- 
If a variable with the same name is defined inside the scope of the function 
as well then it will print the value given inside the function only and not the global value.
# This function has a variable with
# name same as s.
def f():
  s = "Me too."
  print(s)

# Global scope
s = "I love Geeksforgeeks"
f()
print(s)

Note :-Now, what if we try to change the value of a global variable inside the function?

# This function uses global variable s
def f():
  s += 'GFG'
  print("Inside Function", s)


# Global scope
s = "I love Geeksforgeeks"
f()
--------------------------------------------------------------------------------------------------------------------
To make the above program work, we need to use the “global” keyword in Python. Let’s see what this global keyword is.

----------------------------------------------------------------------------------------------------------------------
The global Keyword

We only need to use the global keyword in a function if we want to do assignments or change the global variable. 
global is not needed for printing and accessing. 
Python “assumes” that we want a local variable due to the assignment to s inside of f(), 
so the first statement throws the error message. 
Any variable which is changed or created inside of a function is local if it hasn’t been declared as a global variable. 
To tell Python, that we want to use the global variable, 
we have to use the keyword “global”

Example 1: Using Python global keyword
# This function modifies the global variable 's'
def f():
  global s
  s += ' GFG'
  print(s)
  s = "Look for Geeksforgeeks Python Section"
  print(s) 

# Global Scope
s = "Python is great!"
f()
print(s)


----------------------------------------------------------------------------------------------------------------------


2) local variables
The variable which is declared inside the function are called as local variables which is scope specific.
Local variables in Python are those which are initialized inside a function and belong only to that particular function.
It cannot be accessed anywhere outside the function. 
Ex1 

note:- Can a local variable be used outside a function?
Ex 2 local variable used outside a function
def f():
  
  # local variable
  s = "I love Geeksforgeeks"
  print("Inside Function:", s)

f()
print(s)
--------------------------------------------------------------------------------------------------------------------------------
Example 2: Using Python global and local variables
a = 1 # global 
# Uses global because there is no local 'a'
def f():
  print('Inside f() : ', a)

# Variable 'a' is redefined as a local
def g():
  a = 2 # local
  print('Inside g() : ', a)

# Uses global keyword to modify global 'a'
def h():
  global a
  a = 3
  print('Inside h() : ', a)


# Global scope
print('global : ', a)
f()
print('global : ', a)
g()
print('global : ', a)
h()
print('global : ', a)

-------------------------------------------------------------------------------------------------------------------------------
# Difference b/w Local Variable Vs. Global Variables

Comparision Basis          Global Variable                            Local Variable
Definition---->declared outside the functions                            declared within the functions
Lifetime------>They are created  the execution of the program begins     They are created when the function starts its execution 
            and are lost when the program is ended                       and are lost when the function ends
                              
Data Sharing  Offers Data Sharing                                       It doesn’t offers Data Sharing
Scope-------> Can be access throughout the code                         Can access only inside the function
Parameters---->parameter passing is not necessary                      parameter passing is necessary
needed           
Storage--->A fixed location selected by the compiler                   They are  kept on the stack
Value----->Once the value changes it is reflected                    once changed the variable don’t affect other functions of the program
           throughout the code             