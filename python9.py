''' Python - Change List Items

Change Item Value
To change the value of a specific item, refer to the index number:

Example
Change the second item:

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
-------------------------------------------------------------------------------
* Change a Range of Item Values

To change the value of items within a specific range, define a list with the new values, 
and refer to the range of index numbers where you want to insert the new values:

Example
Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
----------------------------------------------------------------------------------------
If you insert more items than you replace, the new items will be inserted where you specified, 
and the remaining items will move accordingly:

Example
Change the second value by replacing it with two new values:

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
--------------------------------------------------------------------------------------------------------------------------------------------------------
Note: The length of the list will change when the number of items inserted does not match 
the number of items replaced.
--------------------------------------------------------------------------------------------------------------------------------------------------------
If you insert less items than you replace, the new items will be inserted where you specified, 
and the remaining items will move accordingly:

Example
Change the second and third value by replacing it with one value:

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
-------------------------------------------------------------------------------------------------------------------------------------------
* Insert Items

To insert a new list item, without replacing any of the existing values, 
we can use the insert() method.

The insert() method inserts an item at the specified index:

Example
Insert "watermelon" as the third item:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon") # index number =2,value=watermelon
print(thislist)
------------------------------------------------------------------------------------------------------------------------
* Python - Add List Items

Append Items

To add an item to the end of the list, use the append() method:

Example
Using the append() method to append an item:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
--------------------------------------------------------------------------------------------------------------
Insert Items
To insert a list item at a specified index, use the insert() method.

The insert() method inserts an item at the specified index:

Example
Insert an item as the second position:

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
---------------------------------------------------------------------------------------------------------------
* Extend List

To append elements from another list to the current list, use the extend() method.
The elements will be added to the end of the list.
Example
Add the elements of tropical to thislist:

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
-----------------------------------------------------------------------------------------------------------------
Add Any Iterable

The extend() method does not have to append lists, 
you can add any iterable object (tuples, sets, dictionaries etc.).

Example
Add elements of a tuple to a list:

thislist = ["apple", "banana", "cherry"] #----list
thistuple = ("kiwi", "orange") #--------- tuple
thislist.extend(thistuple)
print(thislist)
-----------------------------------------------------------------------------------------------------------------
* Python - Remove List Items

Remove Specified Item
The remove() method removes the specified item.

Example
Remove "banana":

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
-----------------------------------------------------------------------------------------------------------
If there are more than one item with the specified value, 
the remove() method removes the first occurance:

Example
Remove the first occurance of "banana":

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
-----------------------------------------------------------------------------------------------------------
Remove Specified Index

The pop() method removes the specified index.

Example
Remove the second item:

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

If you do not specify the index, the pop() method removes the last item.

Example
Remove the last item:

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
-----------------------------------------------------------------------------------------------------------
The del keyword also removes the specified index:

Example
Remove the first item:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

The del keyword can also delete the list completely.

Example
Delete the entire list:

thislist = ["apple", "banana", "cherry"]
del thislist

Clear the List

The clear() method empties the list.

The list still remains, but it has no content.
----------------------------------------------------------------------------------------------------------
Example
Clear the list content:

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
---------------------------------------------------------------------------------------------------------
* Python - Loop Lists

Loop Through a List
You can loop through the list items by using a for loop:

Example 1
Print all items in the list, one by one:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

Loop Through the Index Numbers

You can also loop through the list items by referring to their index number.

Use the range() and len() functions to create a suitable iterable.

Example
Print all items by referring to their index number:

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

The iterable created in the example above is [0, 1, 2].
-------------------------------------------------------------------------------------------------------------
Using a While Loop

You can loop through the list items by using a while loop.

Use the len() function to determine the length of the list, 
then start at 0 and loop your way through the list items by referring to their indexes.

Remember to increase the index by 1 after each iteration.

Example 2
Print all items, using a while loop to go through all the index numbers

thislist = ["apple", "banana", "cherry"]
i = 0 ,i=1
while i < len(thislist):
  print(thislist[i])
  i = i + 1
------------------------------------------------------------------------------------------------------------
Looping Using List Comprehension

List Comprehension offers the shortest syntax for looping through lists:

Example
A short hand for loop that will print all items in a list:

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
-------------------------------------------------------------------------------------------------------------
Python - List Comprehension

List Comprehension

List comprehension offers a shorter syntax when you want to create a new list based on the values 
of an existing list.

Example

Based on a list of fruits, you want a new list, 
containing only the fruits with the letter "a" in the name.

Without list comprehension you will have to write a for statement with a conditional test inside:

Example 1 --> without list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

With list comprehension you can do all that with only one line of code:
Example 2

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
--------------------------------------------------------------------------------------------------------
The Syntax :-

newlist = [expression for item in iterable if condition == True]
The return value is a new list, leaving the old list unchanged.

Condition
The condition is like a filter that only accepts the items that valuate to True.
--------------------------------------------------------------------------------------------------------
Example 3
Only accept items that are not "apple":

newlist = [x for x in fruits if x != "apple"]
The condition if x != "apple"  will return True for all elements other than "apple", 
making the new list contain all fruits except "apple".

The condition is optional and can be omitted:

Example
With no if statement:

newlist = [x for x in fruits]
-----------------------------------------------------------------------------------------
Iterable

The iterable can be any iterable object, like a list, tuple, set etc.

Example 1
You can use the range() function to create an iterable:

newlist = [x for x in range(10)]
Same example, but with a condition:

Example 2
Accept only numbers lower than 5:

newlist = [x for x in range(10) if x < 5]

Expression
The expression is the current item in the iteration, but it is also the outcome, 
which you can manipulate before it ends up like a list item in the new list:

Example 1
Set the values in the new list to upper case:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"] # exisiting list
newlist = [x.upper() for x in fruits]
print(newlist)
You can set the outcome to whatever you like:

Example 2
Set all values in the new list to 'hello':

newlist = ['hello' for x in fruits]
The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:

Example 3
Return "orange" instead of "banana":
fruits = ["apple", "banana", "cherry", "kiwi", "mango"] # exisiting list
newlist = [x if x != "apple" else "orange" for x in fruits]
print(newlist)
The expression in the example above says:

"Return the item if it is not banana, if it is banana return orange".

---------------------------------------------------------------------------------------------------------------------------------------
* Python - Sort Lists

Sort List Alphanumerically
List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

Example 1
Sort the list alphabetically:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
Example 2
Sort the list numerically:

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

Sort Descending
To sort descending, use the keyword argument reverse = True:

Example 1
Sort the list descending:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
Example 2
Sort the list descending:

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
---------------------------------------------------------------------------------------------------
* Customize Sort Function
You can also customize your own function by using the keyword argument key = function.

The function will return a number that will be used to sort the list (the lowest number first):

Example
Sort the list based on how close the number is to 50:

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
--------------------------------------------------------------------------------------------------------
Case Insensitive Sort
By default the sort() method is case sensitive, resulting in all capital letters being sorted before 
lower case letters:

Example 1
Case sensitive sorting can give an unexpected result:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

Luckily we can use built-in functions as key functions when sorting a list.

So if you want a case-insensitive sort function, use str.lower as a key function:

Example 1
Perform a case-insensitive sort of the list:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
---------------------------------------------------------------------------------------------------
Reverse Order
What if you want to reverse the order of a list, regardless of the alphabet?

The reverse() method reverses the current sorting order of the elements.

Example
Reverse the order of the list items:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
-----------------------------------------------------------------------------------------------------------------
* Python - Copy Lists

Copy a List
You cannot copy a list simply by typing list2 = list1, 
because: list2 will only be a reference to list1, 
and changes made in list1 will automatically also be made in list2.

There are ways to make a copy, one way is to use the built-in List method copy().

Example 1
Make a copy of a list with the copy() method:

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

Another way to make a copy is to use the built-in method list().

Example 2
Make a copy of a list with the list() method:

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

---------------------------------------------------------------------------------------------------------------------------------
Python - Join Lists
Join Two Lists
There are several ways to join, or concatenate, two or more lists in Python.

One of the easiest ways are by using the + operator.

Example 1
Join two list:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

Another way to join two lists is by appending all the items from list2 into list1, one by one:

Example
Append list2 into list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

Or you can use the extend() method, 
where the purpose is to add elements from one list to another list:

Example 
Use the extend() method to add list2 at the end of list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

-------------------------------------------------------------------------------------------------------------------------------------------
Python List count() Method

Example 
Return the number of times the value "cherry" appears in the fruits list:

fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry")

Definition and Usage
The count() method returns the number of elements with the specified value.

Syntax
list.count(value)
Parameter Values
Parameter	Description
value	Required. Any type (string, number, list, tuple, etc.). The value to search for.


Example
Return the number of times the value 9 appears int the list:

points = [1, 4, 2, 9, 7, 8, 9, 3, 1]

x = points.count(9)
