'''Python Dictionaries 
Dictionary is a collection which is ordered** and changeable. 
No duplicate member
Dictionaries are used to store data values in key:value pairs.
Dictionaries are written with curly brackets, and have keys and values:
note:-
As of Python version 3.7, dictionaries are ordered. 
In Python 3.6 and earlier, dictionaries are unordered.

Example 1:- Create and print a dictionary:

thisdict = {
  "brand": "Ford",    # key : value
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#  Dictionary Items
Dictionary items are ordered, changeable, and do not allow duplicates.
Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

Example
Print the "brand" value of the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"]) # pass the key 

# Ordered or Unordered?
As of Python version 3.7, dictionaries are ordered. 
In Python 3.6 and earlier, dictionaries are unordered.
When we say that dictionaries are ordered, it means that the items have a defined order, 
and that order will not change.
Unordered means that the items do not have a defined order, 
you cannot refer to an item by using an index.

Dictionaries are changeable, meaning that we can change, 
add or remove items after the dictionary has been created.

#Duplicates Not Allowed
Dictionaries cannot have two items with the same key:

Example 1
Duplicate values will overwrite existing values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

# Dictionary Length
To determine how many items a dictionary has, use the len() function:

Example2 
Print the number of items in the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(le
(thisdict))

# Dictionary Items - Data Types
The values in dictionary items can be of any data type:

Example
String, int, boolean, and list data types:

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

type()
From Python's perspective, dictionaries are defined as objects with the data type 'dict':

<class 'dict'>
Example
Print the data type of a dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))
---------------------------------------------------------------------------------------------------------------
#The dict() Constructor
It is also possible to use the dict() constructor to make a dictionary.
Example
Using the dict() method to make a dictionary:

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
---------------------------------------------------------------------------------------------------------------------------
Python - Access Dictionary Items
Accessing Items
You can access the items of a dictionary by referring to its key name, inside square brackets:

Example 1
Get the value of the "model" key:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

There is also a method called get() that will give you the same result:

Example 2
Get the value of the "model" key:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")

Get Keys
The keys() method will return a list of all the keys in the dictionary.

Example 3
Get a list of the keys:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.keys()
The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected 
the keys list.

Example 4
Add a new item to the original dictionary, and see that the keys list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change
-----------------------------------------------------------------------------------------
Get Values
The values() method will return a list of all the values in the dictionary.

Example 5
Get a list of the values:

x = thisdict.values()
The list of the values is a view of the dictionary,
 meaning that any changes done to the dictionary will be reflected in the values list.

Example
Make a change in the original dictionary, and see that the values list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change
Example
Add a new item to the original dictionary, and see that the values list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change
--------------------------------------------------------------------------------------------
Get Items
The items() method will return each item in a dictionary, as tuples in a list.

Example
Get a list of the key:value pairs

x = thisdict.items()
The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.

Example 1
Make a change in the original dictionary, and see that the items list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

Example 2
Add a new item to the original dictionary, and see that the items list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["color"] = "red"

print(x) #after the change
---------------------------------------------------------------------------------------------------
Check if Key Exists
To determine if a specified key is present in a dictionary use the in keyword:

Example
Check if "model" is present in the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


