'''  Data Abstraction in Python
Data abstraction is one of the most essential concepts of Python OOPs which is used to hide irrelevant details 
from the user and show the details that are relevant to the users. 
For example when we fill any online form we do not no what are background process of the form is happening 
we are only feeling information in the form.

A simple example of this can be a car. A car has an accelerator, clutch, and break and we all know 
that pressing an accelerator will increase the speed of the car and applying the brake can stop the car 
but we don’t the internal mechanism of the car and how these functionalities can work this detail hiding 
is known as data abstraction.

To understand data abstraction we should be aware of the below basic concepts:

OOP concepts in Python
Classes in Python
Abstract classes in Python

# Importance of Data Abstraction
It enables programmers to hide complex implementation details while just showing users the most crucial data and
functions. This abstraction makes it easier to design modular and well-organized code, makes it simpler to 
understand and maintain, promotes code reuse, and improves developer collaboration.
------------------------------------------------------------------------------------------------------------------
# Data Abstraction in Python
Data abstraction in Python is a programming concept that hides complex implementation details while exposing only 
essential information and functionalities to users. 
In Python, we can achieve data abstraction by using abstract classes and abstract classes can be created using 
abc (abstract base class) module and abstractmethod of abc module.

Abstraction classes in Python
Abstract class is a class in which one or more abstract methods are defined. 
When a method is declared inside the class without its implementation is known as abstract method.
EX
class Form:
    def details():
        pass

Abstract Method: In Python, abstract method feature is not a default feature. To create abstract method and 
abstract classes we have to import the “ABC” and “abstractmethod” classes from abc (Abstract Base Class) library. Abstract method of base class force its child class to write the implementation of the all abstract methods defined in base class. If we do not implement the abstract methods of base class in the child class then our code will give error. In the below code method_1 is a abstract method created using @abstractmethod decorator.

example
from abc import ABC, abstractmethod
class BaseClass(ABC):
    @abstractmethod
    def method_1(self):
         #empty body
         pass


Concrete Method: Concrete methods are the methods defined in an abstract base class with their complete 
implementation. Concrete methods are required to avoid reprication of code in subclasses. 
For example, in abstract base class there may be a method that implementation is to be same in all its subclasses,
so we write the implementation of that method in abstract base class after 
which we do not need to write implementation of the concrete method again and again in every subclass. 
In the below code startEngine is a concrete method.
Example

class Car(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.engine_started = True

    def startEngine(self):
        if not self.engine_started:
            print(f"Starting the {self.model}'s engine.")
            self.engine_started = True
        else:
            print("Engine is already running.")

Steps to Create Abstract Base Class and Abstract Method:

1> Firstly, we import ABC and abstractmethod class from abc (Abstract Base Class) library.
2> Create a BaseClass that inherits from the ABC class. 
In Python, when a class inherits from ABC, it indicates that the class is intended to be an abstract base class.
3>Inside BaseClass we declare an abstract method named “method_1” by using “abstractmethod” decorater.
Any subclass derived from BaseClass must implement this method_1 method. 
We write pass in this method which indicates that there is no code or logic in this method.   

example 
from abc import ABC, abstractmethod
class BaseClass(ABC):
    @abstractmethod
    def method_1(self):
         #empty body
         pass             

#example of data abstraction
# Python program demonstrate  
# abstract base class work   
from abc import ABC, abstractmethod   
class Car(ABC):   
    def mileage(self):   
        pass  
  
class Tesla(Car):   
    def mileage(self):   
        print("The mileage is 30kmph")   
class Suzuki(Car):   
    def mileage(self):   
        print("The mileage is 25kmph ")   
class Duster(Car):   
     def mileage(self):   
          print("The mileage is 24kmph ")   
  
class Renault(Car):   
    def mileage(self):   
        print("The mileage is 27kmph ")   
          
# Driver code   
t= Tesla ()   
t.mileage()   
  
r = Renault()   
r.mileage()   
  
s = Suzuki()   
s.mileage()

d = Duster()   
d.mileage() 

Explanation -
----------------------------------------------------------------------------------------------------------------
In the above code, we have imported the abc module to create the abstract base class. We created the Car class 
that inherited the ABC class and defined an abstract method named mileage(). 
We have then inherited the base class from the three different subclasses and implemented 
the abstract method differently. We created the objects to call the abstract method.
----------------------------------------------------------------------------------------------------------------
Points to Remember
An Abstract class can contain the both method normal and abstract method.
An Abstract cannot be instantiated; we cannot create objects for the abstract class.
Abstraction is essential to hide the core functionality from the users.
We have covered the all the basic concepts of Abstraction in Python.
---------------------------------------------------------------------------------------------------------------- 