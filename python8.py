''' Python Collections (Arrays)

There are four collection data types in the Python programming language:

1> List is a collection which is ordered and changeable. 
Allows duplicate members.

2> Tuple is a collection which is ordered and unchangeable. 
Allows duplicate members.

3> Set is a collection which is unordered, unchangeable*, and unindexed.
No duplicate members.

4> Dictionary is a collection which is ordered** and changeable. 
No duplicate member
-----------------------------------------------------------------------------
1 Python lists

Lists are used to store multiple items in a single variable.
Lists are created using square brackets: [ ]
Ex thislist = ['boy','girl','suresh']
              print(thislist)

* List items
List items are ordered, changeable, and allow duplicate values.
List items are indexed, the first item has index [0], the second item has index [1] etc.

* Ordered
When we say that lists are ordered, it means that the items have a defined order, 
and that order will not change.
If you add new items to a list, the new items will be placed at the end of the list.

* Changeable
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

* Allow Duplicates
Since lists are indexed, lists can have items with the same value:

Ex thislist = ["apple", "banana", "cherry", "apple", "cherry"]
   print(thislist)

* List Length
To determine how many items a list has, use the len() function:

Example
Print the number of items in the list:

thislist = ["apple", "banana", "cherry"]
print(len(thislist))
---------------------------------------------------------------------------
* List Items - Data Types
List items can be of any data type:

Example
String, int and boolean data types:

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

* A list can contain different data types:

Example
A list with strings, integers and boolean values:

list1 = ["abc", 34, True, 40, "male"]
print(list1)

type() ------ this is a function
From Python's perspective, lists are defined as objects with the data type 'list':

<class 'list'>

Example
What is the data type of a list?

mylist = ["apple", "banana", "cherry"]
print(type(mylist))
-------------------------------------------------------------------------------------------
* The list() Constructor 
It is also possible to use the list() constructor when creating a new list.

Example
Using the list() constructor to make a List:

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

* Python - Access List Items

Access Items

List items are indexed and you can access them by referring to the index number:

The first item has index 0.
Example
Print the second item of the list:

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist[2])

* Negative Indexing
Negative indexing means start from the end

-1 refers to the last item, -2 refers to the second last item etc.

Example
Print the last item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

* Range of Indexes
You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new list with the specified items.

Example
Return the third, fourth, and fifth item:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

* This example returns the items from the beginning to, but NOT including, "kiwi":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
#This will return the items from index 0 to index 4.
#Remember that index 0 is the first item, and index 4 is the fifth item
#Remember that the item in index 4 is NOT included

* By leaving out the end value, the range will go on to the end of the list:

Example
This example returns the items from "cherry" to the end:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

Range of Negative Indexes
Specify negative indexes if you want to start the search from the end of the list:

Example
This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

* Check if Item Exists

To determine if a specified item is present in a list use the in keyword:

Example
Check if "apple" is present in the list:

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

create a list with int number from 1 to 20 and print 2nd last number in list
create a list with float number and print values from start index
create a list with string where age gender and phone number should be present 
create a list with data type of float, string, intger values and range the numbers where last and sound last item should be persent  