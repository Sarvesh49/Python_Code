 '''Python Indentation
Indentation refers to the spaces at the beginning of a code line.

Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.

Python uses indentation to indicate a block of code.

Example 

if 6>2:
	print("six is greater than 2!") 	

python will give error if you skip the indentation	
--------------------------------------------------------------------------------------------------------------
* comments in Python
Python has commenting capability for the purpose of in-code documentation.
Comments can be used to explain Python code.
Comments can be used to make the code more readable.
Comments can be used to prevent execution when testing code.
Comments start with a #, and Python will render the rest of the line as a comment:
Comments can be placed at the end of a line
Example
a=1
b=2
c=a+b # This is comment
* Multilne comments
Python does not really have a syntax for multiline comments.
To add a multiline comment you could insert a # for each line: 
                               OR
you can use a multiline string.

Since Python will ignore string literals that are not assigned to a variable, you can add 
a multiline string (triple quotes) in your code, and place your comment inside it:

EX
'''
#------------------------------------------------------
'''
This is a multiline comment
'''