'''Python Data Types

Built-in Data Types
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:
-----------------------------------------------------
Text Type:	str ---1                                     
Numeric Types:	int, float, complex   ---1               
Sequence Types:	list, tuple, range ---2    
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool ----1
Binary Types:	bytes, bytearray, memoryview ---1
None Type:	NoneType  ----0
----------------------------------------------------
Python Numbers
There are three numeric types in Python:

int --- Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
float ----- Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
complex ---- Complex numbers are written with a "j" as the imaginary part:
Variables of numeric types are created when you assign a value to them:
Ex
x = 1    # int
y = 2.8  # float
z = 1j   # complex
----------------------------------------------------------------------------------------------------------------------------
# Type Conversion
You can convert from one type to another with the int(), float(), and complex() methods:
You cannot convert complex numbers into another number type.
There are two types of type conversion in Python.

* Implicit Conversion - automatic type conversion
* Explicit Conversion - manual type conversion

1 Python Implicit Type Conversion

In certain situations, Python automatically converts one data type to another. 
This is known as implicit type conversion.
let's see an example 
where Python promotes the conversion of the lower data type (integer) to 
the higher data type (float) to avoid data loss.

integer_number = 123
float_number = 1.23

new_number = integer_number + float_number

# display new value and resulting data type
print("Value:",new_number)
print("Data Type:",type(new_number))

# output 
Value: 124.23
Data Type: <class 'float'>
In the above example, we have created two variables: integer_number and float_number of 
int and float type respectively.

Then we added these two variables and stored the result in new_number.

As we can see new_number has value 124.23 and is of the float data type.

It is because Python always converts smaller data types to larger data types to avoid the loss of data.

Note:
We get TypeError, if we try to add str and int. For example, '12' + 23. 
Python is not able to use Implicit Conversion in such conditions.
Python has a solution for these types of situations which is known as Explicit Conversion.
----------------------------------------------------------------------------------------------------
*Explicit Type Conversion
In Explicit Type Conversion, users convert the data type of an object to required data type.

We use the built-in functions like int(), float(), str(), etc to perform explicit type conversion.

This type of conversion is also called typecasting because the user casts (changes) the data type of the objects.

Convert from one type to another:
Ex 1
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
----------------------------------------------------------------
Example 2: Addition of string and integer Using Explicit Conversion
num_string = '12'
num_integer = 23

print("Data type of num_string before Type Casting:",type(num_string))

# explicit type conversion
num_string = int(num_string)

print("Data type of num_string after Type Casting:",type(num_string))

num_sum = num_integer + num_string

print("Sum:",num_sum)
print("Data type of num_sum:",type(num_sum))

# Output

Data type of num_string before Type Casting: <class 'str'>
Data type of num_string after Type Casting: <class 'int'>
Sum: 35
Data type of num_sum: <class 'int'>
------------------------------------------------------------------------------------------------------
In the above example, we have created two variables: num_string and num_integer with str and int type values 
respectively. 
Notice the code,

num_string = int(num_string)
Here, we have used int() to perform explicit type conversion of num_string to integer type.

After converting num_string to an integer value, Python is able to add these two variables.

Finally, we got the num_sum value i.e 35 and data type to be int.
---------------------------------------------------------------------------------------------------------------------------------
Key Points to Remember
1 Type Conversion is the conversion of an object from one data type to another data type.
2 Implicit Type Conversion is automatically performed by the Python interpreter.
3 Python avoids the loss of data in Implicit Type Conversion.
4 Explicit Type Conversion is also called Type Casting, the data types of objects are converted using predefined functions by the user.
5 In Type Casting, loss of data may occur as we enforce the object to a specific data type.

-----------------------------------------------------------------
* Python Basic Input and Output

* Python Output

In Python, we can simply use the print() function to print output. For example,

print('Python is powerful')

# Output: Python is powerful

Here, the print() function displays the string enclosed inside the single quotation.

Syntax of print()

In the above code, the print() function is taking a single parameter.

However, the actual syntax of the print function accepts 5 parameters

print(object= separator= end= file= flush=)
Here,

object - value(s) to be printed 
sep (optional) - allows us to separate multiple objects inside print().
end (optional) - allows us to add add specific values like new line "\n", tab "\t"
file (optional) - where the values are printed. It's default value is sys.stdout (screen)
flush (optional) - boolean specifying if the output is flushed or buffered. Default: False
-----------------------------------------------------------------------------------------------
Example 1: Python Print Statement
print('Good Morning!')
print('It is rainy today')

Output

Good Morning!
It is rainy today
In the above example, the print() statement only includes the object to be printed. 
Here, the value for end is not used. Hence, it takes the default value '\n'.

So we get the output in two different lines.
--------------------------------------------------------------------------------------------------
Example 2: Python print() with end Parameter
# print with end whitespace
print('Good Morning!', end= ' ')

print('It is rainy today')

Output

Good Morning! It is rainy today
Notice that we have included the end= ' ' after the end of the first print() statement.

Hence, we get the output in a single line separated by space.
----------------------------------------------------------------------------------------------------
Example 3: Python print() with sep parameter

print('New Year', 2023, 'See you soon!', sep= '. ')

Output

New Year. 2023. See you soon!
 
In the above example, the print() statement includes multiple items separated by a comma.

Notice that we have used the optional parameter sep= ". " inside the print() statement.

Hence, the output includes items separated by . not comma.
----------------------------------------------------------------------------------------------------
Example: Print Python Variables and Literals
We can also use the print() function to print Python variables. For example,

number = -10.6

name = "Program"

# print literals     
print(5)

# print variables
print(number)
print(name)

Output

5
-10.6
---------------------------------------------------------------------------------------------------------
Example: Print Concatenated Strings
We can also join two strings together inside the print() statement. For example,

print('Program is ' + 'awesome.')

Output

Program is awesome.
Here,

the + operator joins two strings 'Program is ' and 'awesome.'
the print() function prints the joined string
----------------------------------------------------------------------------------------------------------
* Output formatting
Sometimes we would like to format our output to make it look attractive. 
This can be done by using the str.format() method. For example,

x = 5
y = 10

print('The value of x is {} and y is {}'.format(x,y))

Here, the curly braces {} are used as placeholders. 
We can specify the order in which they are printed by using numbers (tuple index).
----------------------------------------------------------------------------------------------------------
*   Python Input
While programming, we might want to take the input from the user.
In Python, we can use the input() function.

Syntax of input()

input(prompt)
Here, prompt is the string we wish to display on the screen. It is optional.

Example: Python User Input
# using input() to take user input
num = input('Enter a number: ')

print('You Entered:', num)

print('Data type of num:', type(num))

# Output
Enter a number: 10
You Entered: 10
Data type of num: <class 'str'>
In the above example, we have used the input() function to take input
from the user and stored the user input in the num variable.

It is important to note that the entered value 10 is a string, not a number. So, type(num) returns <class 'str'>.

To convert user input into a number we can use int() or float() or complex(), str() functions as:

num = int(input('Enter a number: '))
num1=float(input('Enter the float value : '))
num3=complex(input('Enter a complex number: '))
Here, the data type of the user input is converted from string to integer .
EX :-

num = int(input('Enter a number: '))
print(num)
print(type(num))

num1=float(input("Enter the float value :"))
print(num1)
print(type(num1))

num3=complex(input("Enter the complex values : "))
print(num3)
print(type(num3))

num4=str(input("Enter tha string value :"))
print(num4)
print(type(num4))

