'''
Python Inheritance
Inheritance is an important aspect of the object-oriented paradigm or concept 
Inheritance provides code reusability to the program because we can use an existing class to create 
a new class instead of creating it from scratch.

In inheritance, the child class acquires the properties and can access all the data members 
and functions defined in the parent class.

Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.


Create a Parent Class
Any class can be a parent class, so the syntax is the same as creating any other class:

Example
Create a class named Person, with firstname and lastname properties, and a printname method:

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

# Create a Child Class
To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:

Example
Create a class named Student, which will inherit the properties and methods from the Person class:

class Student(Person):
  pass

#Note: Use the pass keyword when you do not want to add any other properties or methods to the class.
Now the Student class has the same properties and methods as the Person class.

Example
Use the Student class to create an object, and then execute the printname method:

x = Student("Mike", "Olsen")
x.printname()
-----------------------------------------------------------------------------------------------------------------------------
Add the __init__() Function
So far we have created a child class that inherits the properties and methods from its parent.

We want to add the __init__() function to the child class (instead of the pass keyword).

Note: The __init__() function is called automatically every time the class is being used to create a new object.

Example
Add the __init__() function to the Student class:

class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.
When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

# Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.

To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

Example
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
Now we have successfully added the __init__() function, and kept the inheritance of the parent class, and we are ready to add functionality in the __init__() function.

Use the super() Function
Python also has a super() function that will make the child class inherit all the methods and properties 
from its parent:

Example
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.

#   Add Properties
Example
Add a property called graduationyear to the Student class:

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019
In the example below, the year 2019 should be a variable, and passed into the Student class when creating student objects. To do so, add another parameter in the __init__() function:

Example
Add a year parameter, and pass the correct year when creating objects:

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
Add Methods
Example
Add a method called welcome to the Student class:

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.

-----------------------------------------------------------------------------------------------------------------------------
#  Types of inheritance
1 single inheritance
2 Multiple inheritance
3 multilevel inhertiance
4 Hierarchical Inheritance
5 Hybrid Inheritance

1 single inhertiance
Single inheritance enables a derived class to inherit properties from a single parent class,
thus enabling code reusability and the addition of new features to existing code.

[parent class/ base class ]A -------------> B [ child class/ derived class]

Ex Python program to demonstrate
# single inheritance
 
# Base class
class Parent:
    def func1(self):
        print("This function is in parent class.")
# Derived class
class Child(Parent):
    def func2(self):
        print("This function is in child class.")

object = Child()
object.func1()
object.func2()



2 Multiple Inheritance: 

When a class can be derived from more than one base class this type of inheritance 
is called multiple inheritances.In multiple inheritances, 
all the features of the base classes are inherited into the derived class. 
                                   OR
When a child class inherits from multiple parent classes, it is called multiple inheritances.                                    


[base class / parent class]A    and   [base class / parent class]B-----------|
            |                                                                |
            |                                                                |
            |-------------->[child class/ derived class] C <-----------------|


Ex Python program to demonstrate
# multiple inheritance

# Base class1
class Mother:
  mothername = ""
  def mother(self):
    print(self.mothername)

# Base class2
class Father:
  fathername = ""

  def father(self):
    print(self.fathername)

Derived class/ child class

class Son(Mother, Father):
  def parents(self):
    print("Father :", self.fathername)
    print("Mother :", self.mothername)

# createing object and calling function 
s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()

3 Multilevel Inheritance :
In multilevel inheritance, features of the base class and the derived class are further inherited into the new derived class. 
This is similar to a relationship representing a child and a grandfather. 
                                                 OR
When we have a child and grandchild relationship. This means that a child class will inherit from its parent class, 
which in turn is inheriting from its parent class.

[base class/parent class]A---------->[intermediatory class]B---------->[derived class/ child class] C

# Python program to demonstrate
# multilevel inheritance

# Base class
class Grandfather:

  def __init__(self, grandfathername):
    self.grandfathername = grandfathername

# Intermediate class

class Father(Grandfather):
  def __init__(self, fathername, grandfathername):
    self.fathername = fathername

    # invoking constructor of Grandfather class
    Grandfather.__init__(self, grandfathername)

# Derived class

class Son(Father):
  def __init__(self, sonname, fathername, grandfathername):
    self.sonname = sonname

    # invoking constructor of Father class
    Father.__init__(self, fathername, grandfathername)

  def print_name(self):
    print('Grandfather name :', self.grandfathername)
    print("Father name :", self.fathername)
    print("Son name :", self.sonname)

s1 = Son('Prince', 'Rampal', 'Lal mani')
print(s1.grandfathername)
s1.print_name()


4 Hierarchical Inheritance: 
When more than one derived class are created from a single base this type of inheritance is called hierarchical inheritance. 
In this program, we have a parent (base) class and two child (derived) classes.
                                              OR
More than one derived class can be created from a single base or parent class        
                                   [base class/parent class]A 
_____________________________________________|_______________________________________________________
|                                            |                                                       |
[derived class/ child class] B         [derived class/ child class] C           [derived class/ child class] D


# Python program to demonstrate
# Hierarchical inheritance

# Base class
class Parent:
  def func1(self):
    print("This function is in parent class.")

# Derived class1

class Child1(Parent):
  def func2(self):
    print("This function is in child 1.")

# Derivied class2

class Child2(Parent):
  def func3(self):
    print("This function is in child 2.")

object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()

5 Hybrid Inheritance

Inheritance consisting of multiple types of inheritance is called hybrid inheritance. 
                                                OR 
This form combines more than one form of inheritance. Basically, it is a blend of more than one type of inheritance.


# Python program to demonstrate
# hybrid inheritance

class School:
    def func1(self):
        print("This function is in school.")
 
class Student1(School):
    def func2(self):
        print("This function is in student 1. ")
 
class Student2(School):
    def func3(self):
        print("This function is in student 2.")
 
class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")
 
object = Student3()
object.func1()
object.func2()

'''
