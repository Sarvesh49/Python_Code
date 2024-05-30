'''Python RegEx
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

RegEx can be used to check if a string contains the specified search pattern.

RegEx Module
Python has a built-in package called re, which can be used to work with Regular Expressions.

Import the re module:

import re
RegEx in Python
When you have imported the re module, you can start using regular expressions:

Example
Search the string to see if it starts with "The" and ends with "Spain":

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
------------------------------------------------------------------------------------------------------------
RegEx Functions
The re module offers a set of functions that allows us to search a string for a match:

Function	                               Description
findall-------------->	Returns a list containing all matches # database 
search-------------->	Returns a Match object if there is a match anywhere in the string
split-------------->	Returns a list where the string has been split at each match
sub-------------->	    Replaces one or many matches with a string

-----------------------------------------------------------------------------------------------------------

Metacharacters
Metacharacters are characters with a special meaning:

Character	                       Description	                            Examples	
[]	                          A set of characters	                        "[a-m]"	
\                          Signals a special sequence 
               (can also be used to escape special characters)	              "\d"

^	                          Starts with	                                "^hello"	
$	                           Ends with	                                "planet$"
------------------------------------------------------------------------------------------
Ex1

import re

txt = "The rain in Spain"

#Find all lower case characters alphabetically between "a" and "m":

x = re.findall("[a-m]", txt)
print(x)
---------------------------------------------------------------------------------------------------------------
Ex2
import re

txt = "That will be 59 dollars"

#Find all digit characters:

x = re.findall("\d", txt)
print(x)
--------------------------------------------------------------------------------------------------------------
EX3
import re

txt = "hello planet"

#Check if the string starts with 'hello':

x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match found")
-------------------------------------------------------------------------------------------------------------
Ex4
import re

txt = "hello planet"

#Check if the string ends with 'planet':

x = re.findall("planet$", txt)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")
----------------------------------------------------------------------------------------------------------
The findall() Function
The findall() function returns a list containing all matches.

Example
Print a list of all matches:

import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
The list contains the matches in the order they are found.

If no matches are found, an empty list is returned:

Example
Return an empty list if no match was found:

import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)
------------------------------------------------------------------------------------------------------ 
The search() Function

The search() function searches the string for a match, and returns a Match object if there is a match.

If there is more than one match, only the first occurrence of the match will be returned:

Example
Search for the first white-space character in the string:

import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

If no matches are found, the value None is returned:

Example
Make a search that returns no match:

import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)
----------------------------------------------------------------------------------------- 
The split() Function
The split() function returns a list where the string has been split at each match:

Example
Split at each white-space character:

import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
You can control the number of occurrences by specifying the maxsplit parameter:

Example
Split the string only at the first occurrence:

import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)
--------------------------------------------------------------------------------------- 
The sub() Function

The sub() function replaces the matches with the text of your choice:

Example
Replace every white-space character with the number 9:

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

You can control the number of replacements by specifying the count parameter:

Example
Replace the first 2 occurrences:

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)
------------------------------------------------------------------------------------------ 
Match Object
A Match Object is an object containing information about the search and the result.

Note: If there is no match, the value "None" will be returned, instead of the Match Object.
there are three methods that we can use on match object
1 start()-->method return start index of the matching
2 end()-->method return last index of the matching
3 group()--> this return the matching string of group

Example
Do a search that will return a Match Object:

import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object
The Match object has properties and methods used to retrieve information about the search, and the result:

.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match
Example
Print the position (start- and end-position) of the first match occurrence.

The regular expression looks for any words that starts with an upper case "S":

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
Example 2
Print the string passed into the function:

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)
Example 3
Print the part of the string where there was a match.

The regular expression looks for any words that starts with an upper case "S":

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
Note: If there is no match, the value None will be returned, instead of the Match Object.



Examples on REgular expersion
import re

a=input("enter string to perfrom match operation :")
mtch=re.search(a,"pythonissdymnaiclaaa")
print(mtch)
if mtch!=None:
    print(mtch.start()," ",mtch.end())
else:
  print("there is no matching at any level")   
-------------------------------------------------------------
import re
mtch=re.findall('[0-9]','abch3hdh5bk6')
print(mtch) 
----------------------------------------------------------
import re
mtch=re.findall('[a-zA-z]','AbaZS1')
print(mtch) 
-----------------------------------------------------------
import re
obj=re.sub('[0-7]','@','ab3gd6nklp')
print(obj)
----------------------------------------------------------
import re
mo=input("Enter the mobile number:")
obj=re.fullmatch('[0-7]\d{9}',mo) # 0,1,2,3,4,5,6,7,8,9\d
if obj!=None:
  print("vaild mobile number")
else:
  print("invaild mobile number")
----------------------------------------------------------         

finditer() this return iterating object which match the object for every match from left to right 
direction
synatx:--
objmatch=patternobj.finditer("pythonispython")

Ex
import re
count=0
match=re.finditer("Hi","HiaHiHiaHi")
for i in match: # loop 4 times exeute
  count+=1
  print(i.start()," ",i.end()," ",i.group())
print("The number of occurrence :",count) ''' 