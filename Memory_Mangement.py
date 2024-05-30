'''Understanding Memory allocation is important to any software developer as writing efficient code means
writing a memory-efficient code. Memory allocation can be defined as allocating a block of space 
in the computer memory to a program. In Python memory allocation and deallocation method is automatic 
as the Python developers created a garbage collector for Python so that the user does 
not have to do manual garbage collection.

Python uses two strategies for memory allocation: 

Garbage collection
Reference counting


Garbage Collection
Garbage collection is a process in which the interpreter frees up the memory when not in use to make it available for other objects.
Assume a case where no reference is pointing to an object in memory i.e. it is not in use so, 
the virtual machine has a garbage collector that automatically deletes that object from the heap memory
It helps prevent memory leaks, optimize memory usage, and ensure efficient memory allocation for the program.

Generational Garbage Collection

When attempting to add an object to a reference counter, a cyclical reference or reference cycle is produced. 
Because the object’s reference counter could never reach 0 (due to cycle), a reference counter cannot destroy the object. 
Therefore, in situations like this, we employ the universal waste collector.
It operates and releases the memory used. A Generational Garbage Collector can be found in the standard library’s gc module.

Automatic Garbage Collection of Cycles

Because reference cycles take computational work to discover, garbage collection must be a scheduled activity. 
Python schedules garbage collection based upon a threshold of object allocations and object deallocations. 
When the number of allocations minus the number of deallocations is greater than the threshold number, 
the garbage collector is run. One can inspect the threshold for new objects (objects in Python known as generation 0 objects) 
by importing the gc module and asking for garbage collection thresholds: 
 
Number of allocations-Number of deallocations > threshold number----> garbage collector is activated.

# loading gc
import gc
 
# get the current collection 
# thresholds as a tuple
print("Garbage collection thresholds:",
                    gc.get_threshold())
output:-
Garbage collection thresholds: (700, 10, 10)

Here, the default threshold on the above system is 700. This means when the number of allocations vs. 
the number of deallocations is greater than 700 the automatic garbage collector will run. 
Thus any portion of your code which frees up large blocks of memory is a good candidate for running manual garbage collection. 

Manual Garbage Collection
Invoking the garbage collector manually during the execution of a program can be a good idea for how to handle memory 
being consumed by reference cycles.

The garbage collection can be invoked manually in the following way: 

# Importing gc module
import gc
 
# Returns the number of
# objects it has collected
# and deallocated
collected = gc.collect()
 
# Prints Garbage collector 
# as 0 object
print("Garbage collector: collected",
          "%d objects." % collected)


If few cycles are created, then how manual collection works: 
Example: 

import gc
i = 0
 
# create a cycle and on each iteration x as a dictionary
# assigned to 1
def create_cycle():
    x = { }
    x[i+1] = x
    print(x)
 
# lists are cleared whenever a full collection or 
# collection of the highest generation (2) is run
collected = gc.collect() # or gc.collect(2)
print("Garbage collector: collected %d objects." % (collected))
 
print("Creating cycles...")
for i in range(10):
    create_cycle()
 
collected = gc.collect()
 
print("Garbage collector: collected %d objects." % (collected))
------------------------------------------------------------------------------------------------------------------------------
here are two ways for performing manual garbage collection: 
time-based and event-based garbage collection. 

Time-based garbage collection is simple: the garbage collector is called after a fixed time interval. 
Event-based garbage collection calls the garbage collector on event occurrence.
For example, when a user exits the application or when the application enters into an idle state. 
-----------------------------------------------------------------------------------------------------------------------------
Forced Garbage Collection
In Python, the garbage collector runs automatically and periodically to clean up objects that are no longer
referenced and thus are eligible for garbage collection. However, in some cases,
you may want to force garbage collection to occur immediately. You can do this using the gc. collect() 
function provided by the gc module.

Example :

import gc
 
# Create some objects
obj1 = [1, 2, 3]  # list
obj2 = {"a": 1, "b": 2}  # dic
obj3 = "Hello, world!"  #string
 
# Delete references to objects
del obj1
del obj2
del obj3
 
# Force a garbage collection
gc.collect()

# Disabling Garbage Collection

In Python, the garbage collector is enabled by default and automatically runs periodically to 
clean up objects 
that are no longer referenced and thus are eligible for garbage collection. 
However, in some cases, you may want to disable the garbage collector to prevent it from running.
You can do this using the gc.disable() function provided by the gc module.

import gc
 
# Disable the garbage collector
gc.disable()
 
# Create some objects
obj1 = [1, 2, 3]
obj2 = {"a": 1, "b": 2}
obj3 = "Hello, world!"
 
# Delete references to objects
del obj1
del obj2
del obj3
 
# The garbage collector is disabled, so it will not run

Interacting with Python Garbage Collector
A built-in mechanism called the Python garbage collector automatically eliminates objects that are no longer 
referenced in order to free up memory and stop memory leaks. 
The Python gc module offers a number of ways to interact 
with the garbage collector, which is often executed automatically.

1. Enabling and disabling the garbage collector: You can enable or disable the garbage collector using the 
gc.enable()
and gc. disable() functions, respectively. 
Example:

import gc
 
# Disable the garbage collector
gc.disable()
 
# Enable the garbage collector
gc.enable()

2. Forcing garbage collection: You can manually trigger a garbage collection using the gc. collect() function. 
This can be useful in cases where you want to force immediate garbage collection instead of waiting for 
automatic garbage collection to occur. 

Example:

import gc
 
# Trigger a garbage collection
gc.collect()

3. Inspecting garbage collector settings:
You can inspect the current settings of the garbage collector using 
the gc.get_threshold()
function, which returns a tuple representing the current thresholds for generations 0, 1, and 2. 

Example:

import gc
# Get the current garbage collector thresholds
thresholds = gc.get_threshold()
print(thresholds)
Output :

(700, 10, 10)

4. Setting garbage collector thresholds: You can set the thresholds for garbage collection using 
the gc.set_threshold() function. 
This allows you to manually adjust the thresholds for different generations,
which can affect the frequency of garbage collection. 

Example:

import gc
 
gc.set_threshold(500, 5, 5)
print("Garbage collector thresholds set")
 
# Get the current garbage collector thresholds
thresholds = gc.get_threshold()
print("Current thresholds:", thresholds)
-------------------------------------------------------------------------------------------------------------------
Reference counting
Python and various other programming languages employ reference counting, a memory management approach, 
to automatically manage memory by tracking how many times an object is referenced.

A reference count, or the number of references that point to an object, is a property of each object in 
the Python language. 
When an object’s reference count reaches zero, it becomes un-referenceable and its memory can be freed up.

Examples :

Example 1: Simple Reference Counting

# Create an object
x = [1, 2, 3]

# Increment reference count
y = x

# Decrement reference count
y = None

---------------------------------------------------------------
Example 2: Reference Counting with Cyclic Reference

# Create two objects that refer to each other
x = [1, 2, 3]
y = [4, 5, 6]
x.append(y)
y.append(x)

-----------------------------------------------------------------
Example 3: Using the sys.getrefcount() function

import sys
 
# Create an object
x = [1, 2, 3]
 
# Get reference count
ref_count = sys.getrefcount(x)
 
print("Reference count of x:", ref_count)