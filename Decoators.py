'''Decorators in Python
Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behaviour 
of a function or class. Decorators allow us to wrap another function in order to extend the behaviour of 
the wrapped function,without permanently modifying it. But before diving deep into decorators 
let us understand some concepts that will come in handy in learning the decorators.
------------------------------------------------------------------------------------------------------------
First Class Objects
In Python, functions are first class objects which means that functions in Python can be used or passed 
as arguments.
Properties of first class functions:
A function is an instance of the Object type.
You can store the function in a variable.
You can pass the function as a parameter to another function.
You can return the function from a function.
You can store them in data structures such as hash tables, lists, …
-----------------------------------------------------------------------------------------------------------
Consider the below examples for better understanding.

Example 1: Treating the functions as objects. 

# Python program to illustrate functions 
# can be treated as objects 
def shout(text): 
	return text.upper() 

print(shout('Hello')) 

yell = shout 

print(yell('Hello')) 

In the above example, we have assigned the function shout to a variable. 
This will not call the function instead it takes the function object referenced by a shout 
and creates a second name pointing to it, yell.

Example 2: Passing the function as an argument 

# Python program to illustrate functions 
# can be passed as arguments to other functions 
def shout(text): 
	return text.upper() 

def whisper(text): 
	return text.lower() 

def greet(func): 
	# storing the function in a variable 
	greeting = func("""Hi, I am created by a function passed as an argument.""") 
	print (greeting) 

greet(shout) 
greet(whisper) 

In the above example, the greet function takes another function as a parameter (shout and whisper in this case).
The function passed as an argument is then called inside the function greet.

Example 3: Returning functions from another function.

# Python program to illustrate functions 
# Functions can return another function 

def create_adder(x): 
	def adder(y): 
		return x+y 

	return adder 

add_15 = create_adder(15) 

print(add_15(10)) 

In the above example, we have created a function inside of another function and then have returned
the function created inside.
The above three examples depict the important concepts that are needed to understand decorators. 
After going through them let us now dive deep into decorators.
--------------------------------------------------------------------------------------------------------
As stated above the decorators are used to modify the behaviour of function or class. In Decorators,
functions are taken as the argument into another function and then called inside the wrapper function.

Syntax for Decorator: 

@gfg_decorator
def hello_decorator():
    print("Gfg")

Above code is equivalent to -

def hello_decorator():
    print("Gfg")
    
hello_decorator = gfg_decorator(hello_decorator)

In the above code, gfg_decorator is a callable function, 
that will add some code on the top of some another callable function, 
hello_decorator function and return the wrapper function.

Decorator can modify the behaviour:  


# defining a decorator
def hello_decorator(func):

	# inner1 is a Wrapper function in 
	# which the argument is called
	
	# inner function can access the outer local
	# functions like in this case "func"
	def inner1():
		print("Hello, this is before function execution")

		# calling the actual function now
		# inside the wrapper function.
		func()

		print("This is after function execution")
		
	return inner1


# defining a function, to be called inside wrapper
def function_to_be_used():
	print("This is inside the function !!")


# passing 'function_to_be_used' inside the
# decorator to control its behaviour
function_to_be_used = hello_decorator(function_to_be_used)


# calling the function
function_to_be_used()


'''