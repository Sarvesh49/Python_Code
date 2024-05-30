'''Python Polymorphism

The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators 
with the same name that can be executed on many objects or classes.

Function Polymorphism
An example of a Python function that can be used on different objects is the len() function.

String
For strings len() returns the number of characters:

Example
x = "Hello World!"

print(len(x))

Tuple
For tuples len() returns the number of items in the tuple:

Example
mytuple = ("apple", "banana", "cherry")

print(len(mytuple))
Dictionary
For dictionaries len() returns the number of key/value pairs in the dictionary:

Example
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(len(thisdict))
------------------------------------------------------------------------------------------
Polymorphism in Python through Operator Overloading

Operator overloading is another type of polymorphism in which the same operator performs various operations 
depending on the operands. 
Python allows for operator overloading. Let us look at a few built-in Polymorphism in Python examples below:

Polymorphism in + operator:
We already know that the ‘+’ operator is frequently used in Python programs. 
However, it does not have a single application. When you wish to add two integers, 
concatenate two strings, or extend two lists, you use the same + sign. 
The + operator behaves differently depending on the type of object on which it is used.
example

a = 10
b = 20
print('Addition of 2 numbers:', a + b)

str1 = 'Hello '
str2 = 'Python'
print('Concatenation of 2 strings:', str1 + str2)

list1 = [1, 2, 3]
list2 = ['A', 'B']
print('Concatenation of 2 lists:', list1 + list2)
--------------------------------------------------------------------------------------------------
Polymorphism in * operator:
The * operator is used to multiply 2 numbers if the data elements are numeric values. 
If one of the data types is a string, and the other is numeric, 
the string is printed that many times as that of the 2nd variable in the multiplication process.

Example
                   
a = 10
b = 5
print('Multiplication of 2 numbers:', a * b)

num = 3
mystr = 'Python'
print('Multiplication of string:', num * mystr)

------------------------------------------------------------------------------------------
Class Polymorphism

Polymorphism is often used in Class methods, where we can have multiple classes with 
the same method name.

For example, say we have three classes: Car, Boat, and Plane, 
and they all have a method called move():

Example
Different classes with the same method:

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
  x.move()

Look at the for loop at the end. 
Because of polymorphism we can execute the same method for all three classes.

# Inheritance Class Polymorphism(Method Overriding) run time polymorphism

What about classes with child classes with the same name? Can we use polymorphism there?

Yes. If we use the example above and make a parent class called Vehicle, and make Car, Boat, Plane child classes 
of Vehicle, the child classes inherits the Vehicle methods, but can override them:

Example
Create a class called Vehicle and make Car, Boat, Plane child classes of Vehicle:

class Vehicle: # Parent class 
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle): # child class
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()

Child classes inherits the properties and methods from the parent class.

In the example above you can see that the Car class is empty, but it inherits brand, model, and move() from Vehicle.

The Boat and Plane classes also inherit brand, model, and move() from Vehicle, 
but they both override the move() method.

Because of polymorphism we can execute the same method for all classes.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
Compile-Time Polymorphism (Method Overloading)

Method overloading occurs when a class contains many methods with the same name. 
The types and amount of arguments passed by these overloaded methods vary. 
Python does not support method overloading or compile-time polymorphism. 
If there are multiple methods with the same name in a class or Python script, 
the method specified in the latter one will override the earlier one.

Python does not use function arguments in method signatures, hence method overloading is not supported.
'''