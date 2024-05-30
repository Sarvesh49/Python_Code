 '''----------------------------------------------Python Sets---------------------------------------------------------------------

Set is one of 4 built-in data types in Python used to store collections of data, 
the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

Set
Sets are used to store multiple items in a single variable.
Sets are written with curly brackets. { }
A set is a collection which is unordered, unchangeable*, and unindexed.

Example:- Create a Set:
myset = {"apple", "banana", "cherry"}
print(myset)

Note1: Set items are unchangeable, but you can remove items and add new items.
Note2: Sets are unordered, so you cannot be sure in which order the items will appear.
--------------------------------------------------------------------------------------------
Set Items
Set items are unordered, unchangeable, and do not allow duplicate values.

Unordered
Unordered means that the items in a set do not have a defined order.

Set items can appear in a different order every time you use them, 
and cannot be referred to by index or key.

Unchangeable
Set items are unchangeable, meaning that we cannot change the items after the set has been created.

Once a set is created, you cannot change its items, but you can remove items and add new items.

Duplicates Not Allowed
Sets cannot have two items with the same value.
------------------------------------------------------------------------------------------------
Example:-
Duplicate values will be ignored:

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:
      The values False and 0 are considered the same value in sets, and are treated as duplicates:
--------------------------------------------------------------------------------------------------      
Example 1
True and 1 is considered the same value:

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
--------------------------------------------------------------------------------------------------
Example 2
False and 0 is considered the same value:

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)
--------------------------------------------------------------------------------------------------
Get the Length of a Set

To determine how many items a set has, use the len() function.

Example 1
Get the number of items in a set:

thisset = {"apple", "banana", "cherry"}

print(len(thisset))
--------------------------------------------------------------------------------------------------
Set Items - Data Types
Set items can be of any data type:

Example
String, int and boolean data types:

set1 = {"apple", "banana", "cherry"}
print(set1)
set2 = {1, 5, 7, 9, 3}
print(set2)
set3 = {True, False, False}
print(set3)
--------------------------------------------------------------------------------------------------
A set can contain different data types:

Example
A set with strings, integers and boolean values:

set1 = {"abc", 34, True, 40, "male"}

type()
From Python's perspective, sets are defined as objects with the data type 'set':

<class 'set'>

Example
What is the data type of a set?

myset = {"apple", "banana", "cherry"}
print(type(myset))
------------------------------------------------------------------------------------------------------
The set() Constructor

It is also possible to use the set() constructor to make a set.

Example 
Using the set() constructor to make a set:

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
----------------------------------------------------------------------------------------------------
Python - Access Set Items

Access Items
You cannot access items in a set by referring to an index or a key.

But you can loop through the set items using a for loop, 
or ask if a specified value is present in a set, by using the in keyword.
---------------------------------------------------------------------------------------------------
Example 1
Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
---------------------------------------------------------------------------------------------------  
Example 2
Check if "banana" is present in the set:

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

Change Items

Once a set is created, you cannot change its items, but you can add new items.
---------------------------------------------------------------------------------------------------
Python - Add Set Items

Add Items
Once a set is created, you cannot change its items, but you can add new items.

To add one item to a set use the add() method.

Example 1
Add an item to a set, using the add() method:

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

* Add Sets

To add items from another set into the current set, use the update() method.

Example 2

Add elements from tropical into thisset:

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
print(thisset)
-----------------------------------------------------------------------------------------------------
Add Any Iterable

The object in the update() method does not have to be a set, 
it can be any iterable object (tuples, lists, dictionaries etc.).

Example1
Add elements of a list to at set:

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
---------------------------------------------------------------------------------------------------------------
Python - Remove Set Items

Remove Item
To remove an item in a set, use the remove(), or the discard() method.

Example 1
Remove "banana" by using the remove() method:

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")
print(thisset)
-----------------------------------------------------------------------------------------
Note: If the item to remove does not exist, remove() will raise an error.
-----------------------------------------------------------------------------------------
Example 2

Remove "banana" by using the discard() method:

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")
print(thisset)
-----------------------------------------------------------------------------------------
Note: If the item to remove does not exist, discard() will NOT raise an error.
-----------------------------------------------------------------------------------------
You can also use the pop() method to remove an item,
but this method will remove a random item, 
so you cannot be sure what item that gets removed.

The return value of the pop() method is the removed item.

Example 3
Remove a random item by using the pop() method:

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
-------------------------------------------------------------------------------------------------------
Note: Sets are unordered, so when using the pop() method, 
you do not know which item that gets removed.
-------------------------------------------------------------------------------------------------------
Example 4

The clear() method empties the set:

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

Example 5
The del keyword will delete the set completely:

thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)
--------------------------------------------------------------------------------------------------------
Python - Loop Sets

Loop Items
You can loop through the set items by using a for loop:

Example 1
Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
-------------------------------------------------------------------------------------------------------
Python - Join Sets

Join Two Sets

There are several ways to join two or more sets in Python.

You can use the union() method that returns a new set containing all items from both sets,
 or the update() method that inserts all the items from one set into another:

Example 1

The union() method returns a new set with all items from both sets:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

Example 2

The update() method inserts the items in set2 into set1:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
----------------------------------------------------------------------------------------------
Note: Both union() and update() will exclude any duplicate items.
----------------------------------------------------------------------------------------------
Keep ONLY the Duplicates

The intersection_update() method will keep only the items that are present in both sets.

Example 3
Keep the items that exist in both set x, and set y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

The intersection() method will return a new set, 
that only contains the items that are present in both sets.

Example 4

Return a set that contains the items that exist in both set x, and set y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)
print(z)

Keep All, But NOT the Duplicates
The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.

Example 5
Keep the items that are not present in both sets:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

The symmetric_difference() method will return a new set,
 that contains only the elements that are NOT present in both sets.

Example 6
Return a set that contains all items from both sets, except items that are present in both:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)
-------------------------------------------------------------------------------------------------------
Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:
--------------------------------------------------------------------------------------------------------

Example 7

True and 1 is considered the same value:

x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}
z = x.symmetric_difference(y)

print(z)
---------------------------------------------------------------------------------------------------------- 
     