'''Python Datetime
Python Dates
A date in Python is not a data type of its own, but we can import a module named datetime to work with dates
as date objects.

Example
Import the datetime module and display the current date:

import datetime

x = datetime.datetime.now()
print(x)

Date Output
When we execute the code from the example above the result will be:

2024-03-27 10:15:10.109765
The date contains year, month, day, hour, minute, second, and microsecond.

The datetime module has many methods to return information about the date object.

Here are a few examples, you will learn more about them later in this chapter:

Example
Return the year and name of weekday:

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

Creating Date Objects
To create a date, we can use the datetime() class (constructor) of the datetime module.

The datetime() class requires three parameters to create a date: year, month, day.

Example
Create a date object:

import datetime

x = datetime.datetime(2020, 5, 17)

print(x)

The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), 
but they are optional, and has a default value of 0, (None for timezone).
--------------------------------------------------------------------------------------------------------------
Python Math
Python has a set of built-in math functions, including an extensive math module, 
that allows you to perform mathematical tasks on numbers.

Built-in Math Functions
The min() and max() functions can be used to find the lowest or highest value in an iterable:

Example
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)
----------------------------------------------------------------------------------------
The abs() function returns the absolute (positive) value of the specified number:

Example
x = abs(-7.25)

print(x)
------------------------------------------------------------------------
The pow(x, y) function returns the value of x to the power of y (xy).

Example
Return the value of 4 to the power of 3 (same as 4 * 4 * 4):

x = pow(4, 3)

print(x)

-------------------------------------------------------------------------------------------
The Math Module
Python has also a built-in module called math, which extends the list of mathematical functions.

To use it, you must import the math module:

import math
When you have imported the math module, you can start using methods and constants of the module.

The math.sqrt() method for example, returns the square root of a number:

Example
import math

x = math.sqrt(64)

print(x)

The math.ceil() method rounds a number upwards to its nearest integer, 
and the math.floor() method rounds a number downwards to its nearest integer, and returns the result:

Example
import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1

The math.pi constant, returns the value of PI (3.14...):

Example
import math

x = math.pi

print(x)'''