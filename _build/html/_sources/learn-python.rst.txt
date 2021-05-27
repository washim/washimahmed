=========================
Python Getting Started
=========================
Lets start with python learnings and good luck.

Installation
===============
You can install python from here https://www.python.org/downloads/

Hello World
===============
Create helloworld.py file with below program.

.. code:: python
   
   print("Hello, World!")

run helloworld.py in terminal like below

.. code:: shell

   C:/Users/Your Name>python helloworld.py

.. note::

   **C:/Users/Your Name** this will be the actual root folder for your helloworld.py based on the operating system you are using.

Python Comments
=================
Comments starts with a #, and Python will ignore them.

.. code:: python

   #This is a comment
   print("Hello, World!")

Python Variables
=================
Python has no command for declaring a variable. A variable is created the moment you first assign a value to it.

.. code:: python

   x = 5
   y = "John"
   print(x)
   print(y)

.. code:: python
   
   x = 4       # x is of type int
   x = "Sally" # x is now of type str
   print(x)

If you want to specify the data type of a variable, this can be done with casting.

.. code:: python
   
   x = str(3)    # x will be '3'
   y = int(3)    # y will be 3
   z = float(3)  # z will be 3.0

You can get the data type of a variable with the type() function.

.. code:: python

   x = 5
   y = "John"
   print(type(x))
   print(type(y))

String variables can be declared either by using single or double quotes

.. code:: python

   x = "John"
   # is the same as
   x = 'John'

Variable names are case-sensitive.

.. code:: python

   a = 4
   A = "Sally"
   #A will not overwrite a

A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:

* A variable name must start with a letter or the underscore character
* A variable name cannot start with a number
* A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
* Variable names are case-sensitive (age, Age and AGE are three different variables)

Legal variable names:

.. code:: python

   myvar = "John"
   my_var = "John"
   _my_var = "John"
   myVar = "John"
   MYVAR = "John"
   myvar2 = "John"

Illegal variable names:

.. code:: python
   
   2myvar = "John"
   my-var = "John"
   my var = "John"

Each word, except the first, starts with a capital letter called **Camel Case**

.. code:: python
   
   myVariableName = "John"

Each word starts with a capital letter called **Pascal Case**

.. code:: python
   
   MyVariableName = "John"

Each word is separated by an underscore character called **Snake Case**

.. code:: python

   my_variable_name = "John"

Python allows you to assign values to multiple variables in one line:

.. code:: python

   x, y, z = "Orange", "Banana", "Cherry"
   print(x)
   print(y)
   print(z)

And you can assign the same value to multiple variables in one line:

.. code:: python

   x = y = z = "Orange"
   print(x)
   print(y)
   print(z)

If you have a collection of values in a list, tuple etc. Python allows you extract the values into variables. This is called **unpacking**.

.. code:: python

   fruits = ["apple", "banana", "cherry"]
   x, y, z = fruits
   print(x)
   print(y)
   print(z)

The Python print statement is often used to output variables.

.. code:: python

   x = "awesome"
   print("Python is " + x)

Variables that are created outside of a function (as in all of the examples above) are known as global variables. Global variables can be used by everyone, both inside of functions and outside.

.. code:: python

   x = "awesome"
   
   def myfunc():
      print("Python is " + x)
   
   myfunc()

.. note:: Create a variable outside of a function, and use it inside the function

If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

.. code:: python

   x = "awesome"

   def myfunc():
      x = "fantastic"
      print("Python is " + x)

   myfunc()

   print("Python is " + x)

.. note:: Create a variable inside a function, with the same name as the global variable

Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function. To create a global variable inside a function, you can use the global keyword.

.. code:: python

   def myfunc():
      global x
      x = "fantastic"

   myfunc()

   print("Python is " + x)

.. code:: python

   x = "awesome"

   def myfunc():
      global x
      x = "fantastic"

   myfunc()

   print("Python is " + x)

Python Data Types
===================
You can get the data type of any object by using the type() function:

.. code:: python

   x = 5
   print(type(x))

In Python, the data type is set when you assign a value to a variable:

.. csv-table::
   :delim: |
   :file: /_static/data_type.csv
   :widths: 70, 30
   :header-rows: 1

If you want to specify the data type, you can use the following constructor functions:

.. csv-table::
   :delim: |
   :file: /_static/data_type2.csv
   :widths: 70, 30
   :header-rows: 1

Python Strings
===============
Strings in python are surrounded by either single quotation marks, or double quotation marks.

Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

.. code:: python

   a = "Hello"
   print(a)

You can assign a multiline string to a variable by using three quotes:

.. code:: python

   a = """Lorem ipsum dolor sit amet,
   consectetur adipiscing elit,
   sed do eiusmod tempor incididunt
   ut labore et dolore magna aliqua."""
   print(a)

.. code:: python

   a = '''Lorem ipsum dolor sit amet,
   consectetur adipiscing elit,
   sed do eiusmod tempor incididunt
   ut labore et dolore magna aliqua.'''
   print(a)

Get the character at position 1 (remember that the first character has the position 0):

.. code:: python

   a = "Hello, World!"
   print(a[1])

Loop through the letters in the word "banana":

.. code:: python

   for x in "banana":
      print(x)

The len() function returns the length of a string:

.. code:: python

   a = "Hello, World!"
   print(len(a))

Check if "free" is present in the following text:

.. code:: python

   txt = "The best things in life are free!"
   print("free" in txt)

Print only if "free" is present:

.. code:: python

   txt = "The best things in life are free!"
   if "free" in txt:
      print("Yes, 'free' is present.")

Check if "expensive" is NOT present in the following text:

.. code:: python

   txt = "The best things in life are free!"
   print("expensive" not in txt)

print only if "expensive" is NOT present:

.. code:: python

   txt = "The best things in life are free!"
   if "expensive" not in txt:
      print("Yes, 'expensive' is NOT present.")

Get the characters from position 2 to position 5 (not included):

.. code:: python

   b = "Hello, World!"
   print(b[2:5])

Get the characters from the start to position 5 (not included):

.. code:: python

   b = "Hello, World!"
   print(b[:5])

Get the characters from position 2, and all the way to the end:

.. code:: python

   b = "Hello, World!"
   print(b[2:])

Use negative indexes to start the slice from the end of the string:

.. code:: python

   b = "Hello, World!"
   print(b[-5:-2])

The upper() method returns the string in upper case:

.. code:: python

   a = "Hello, World!"
   print(a.upper())

The lower() method returns the string in lower case:

.. code:: python

   a = "Hello, World!"
   print(a.lower())

The strip() method removes any whitespace from the beginning or the end:

.. code:: python

   a = " Hello, World! "
   print(a.strip()) # returns "Hello, World!"

The replace() method replaces a string with another string:

.. code:: python

   a = "Hello, World!"
   print(a.replace("H", "J"))

The split() method splits the string into substrings if it finds instances of the separator:

.. code:: python

   a = "Hello, World!"
   print(a.split(",")) # returns ['Hello', ' World!']

To concatenate, or combine, two strings you can use the + operator.
Merge variable a with variable b into variable c:

.. code:: python

   a = "Hello"
   b = "World"
   c = a + b
   print(c)

To add a space between them, add a " ":

.. code:: python

   a = "Hello"
   b = "World"
   c = a + " " + b
   print(c)

Use the format() method to insert numbers into strings:

.. code:: python

   age = 36
   txt = "My name is John, and I am {}"
   print(txt.format(age))

The format() method takes unlimited number of arguments, and are placed into the respective placeholders:

.. code:: python

   quantity = 3
   itemno = 567
   price = 49.95
   myorder = "I want {} pieces of item {} for {} dollars."
   print(myorder.format(quantity, itemno, price))

You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:

.. code:: python

   quantity = 3
   itemno = 567
   price = 49.95
   myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
   print(myorder.format(quantity, itemno, price))

The escape character allows you to use double quotes when you normally would not be allowed:

.. code:: python

   txt = "We are the so-called \"Vikings\" from the north."

Python Boolians
=================
Booleans represent one of two values: True or False.

.. code:: python

   print(10 > 9)
   print(10 == 9)
   print(10 < 9)

.. code:: python

   a = 200
   b = 33

   if b > a:
      print("b is greater than a")
   else:
      print("b is not greater than a")

.. code:: python

   print(bool("Hello"))
   print(bool(15))

.. code:: python

   x = "Hello"
   y = 15

   print(bool(x))
   print(bool(y))

.. code:: python

   bool("abc")
   bool(123)
   bool(["apple", "cherry", "banana"])

.. code:: python

   bool(False)
   bool(None)
   bool(0)
   bool("")
   bool(())
   bool([])
   bool({})

.. code:: python

   class myclass():
   def __len__(self):
      return 0

   myobj = myclass()
   print(bool(myobj))

.. code:: python

   def myFunction() :
      return True

   print(myFunction())

Print "YES!" if the function returns True, otherwise print "NO!":

.. code:: python

   def myFunction() :
      return True

   if myFunction():
      print("YES!")
   else:
      print("NO!")

Python Operators
=================
Operators are used to perform operations on variables and values.

* Arithmetic operators(`+ - * / % ** //`)
* Assignment operators(`= += -= *= /= %= //= **= &= |= ^= >>= <<=`)
* Comparison operators(`== != > < >= <=`)
* Logical operators(`and or not`)
* Identity operators(`is is not`)
* Membership operators(`in not in`)
* Bitwise operators(`& | ^ ~ << >>`)

Python Lists
==============
Lists are used to store multiple items in a single variable.

Create a List:

.. code:: python

   thislist = ["apple", "banana", "cherry"]
   print(thislist)

Lists allow duplicate values:

.. code:: python

   thislist = ["apple", "banana", "cherry", "apple", "cherry"]
   print(thislist)

Print the number of items in the list:

.. code:: python

   thislist = ["apple", "banana", "cherry"]
   print(len(thislist))

String, int and boolean data types:

.. code:: python

   list1 = ["apple", "banana", "cherry"]
   list2 = [1, 5, 7, 9, 3]
   list3 = [True, False, False]

A list with strings, integers and boolean values:

.. code:: python

   list1 = ["abc", 34, True, 40, "male"]

What is the data type of a list?

.. code:: python

   mylist = ["apple", "banana", "cherry"]
   print(type(mylist))

Using the list() constructor to make a List:

.. code:: python

   thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
   print(thislist)

Print the second item of the list:

.. code:: python

   thislist = ["apple", "banana", "cherry"]
   print(thislist[1])

Print the last item of the list:

.. code:: python

   thislist = ["apple", "banana", "cherry"]
   print(thislist[-1])

Return the third, fourth, and fifth item:

.. code:: python

   thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
   print(thislist[2:5])

This example returns the items from the beginning to, but NOT including, "kiwi":

.. code:: python

   thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
   print(thislist[:4])

This example returns the items from "cherry" to the end:

.. code:: python

   thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
   print(thislist[2:])

This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):

.. code:: python

   thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
   print(thislist[-4:-1])

Check if "apple" is present in the list:

.. code:: python

   thislist = ["apple", "banana", "cherry"]
   if "apple" in thislist:
      print("Yes, 'apple' is in the fruits list")

Change the second item:

.. code:: python

   thislist = ["apple", "banana", "cherry"]
   thislist[1] = "blackcurrant"
   print(thislist)

Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":

.. code:: python

   thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
   thislist[1:3] = ["blackcurrant", "watermelon"]
   print(thislist)

Change the second value by replacing it with two new values:

.. code:: python

   thislist = ["apple", "banana", "cherry"]
   thislist[1:2] = ["blackcurrant", "watermelon"]
   print(thislist)

Change the second and third value by replacing it with one value:

.. code:: python

   thislist = ["apple", "banana", "cherry"]
   thislist[1:3] = ["watermelon"]
   print(thislist)

Insert "watermelon" as the third item:

.. code:: python

   thislist = ["apple", "banana", "cherry"]
   thislist.insert(2, "watermelon")
   print(thislist)

Using the append() method to append an item:

.. code:: python

   thislist = ["apple", "banana", "cherry"]
   thislist.append("orange")
   print(thislist)

Insert an item as the second position:

.. code:: python

   thislist = ["apple", "banana", "cherry"]
   thislist.insert(1, "orange")
   print(thislist)

Add the elements of tropical to thislist:

.. code:: python

   thislist = ["apple", "banana", "cherry"]
   tropical = ["mango", "pineapple", "papaya"]
   thislist.extend(tropical)
   print(thislist)

The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

.. code:: python

   thislist = ["apple", "banana", "cherry"]
   thistuple = ("kiwi", "orange")
   thislist.extend(thistuple)
   print(thislist)

The remove() method removes the specified item.

.. code:: python

   thislist = ["apple", "banana", "cherry"]
   thislist.remove("banana")
   print(thislist)

Remove the second item:

.. code:: python

   thislist = ["apple", "banana", "cherry"]
   thislist.pop(1)
   print(thislist)

Remove the last item:

.. code:: python

   thislist = ["apple", "banana", "cherry"]
   thislist.pop()
   print(thislist)

Remove the first item:

.. code:: python

   thislist = ["apple", "banana", "cherry"]
   del thislist[0]
   print(thislist)

Delete the entire list:

.. code:: python

   thislist = ["apple", "banana", "cherry"]
   del thislist

Clear the list content:

.. code:: python

   thislist = ["apple", "banana", "cherry"]
   thislist.clear()
   print(thislist)

Print all items in the list, one by one:

.. code:: python

   thislist = ["apple", "banana", "cherry"]
   for x in thislist:
      print(x)

Print all items by referring to their index number:

.. code:: python

   thislist = ["apple", "banana", "cherry"]
   for i in range(len(thislist)):
      print(thislist[i])

Print all items, using a while loop to go through all the index numbers

.. code:: python

   thislist = ["apple", "banana", "cherry"]
   i = 0
   while i < len(thislist):
      print(thislist[i])
      i = i + 1

List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

.. code:: python

   fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
   newlist = []

   for x in fruits:
      if "a" in x:
         newlist.append(x)

   print(newlist)

.. code:: python

   fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
   newlist = [x for x in fruits if "a" in x]
   print(newlist)

Sort the list alphabetically:

.. code:: python

   thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
   thislist.sort() # thislist.sort(reverse = True) for descending order
   print(thislist)

You can also customize your own function by using the keyword argument key = function.

.. code:: python

   def myfunc(n):
      return abs(n - 50)

   thislist = [100, 50, 65, 82, 23]
   thislist.sort(key = myfunc)
   print(thislist)

Reverse the order of the list items:

.. code:: python

   thislist = ["banana", "Orange", "Kiwi", "cherry"]
   thislist.reverse()
   print(thislist)

You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

.. code:: python

   thislist = ["apple", "banana", "cherry"]
   mylist = thislist.copy()
   print(mylist)

Make a copy of a list with the list() method:

.. code:: python

   thislist = ["apple", "banana", "cherry"]
   mylist = list(thislist)
   print(mylist)

There are several ways to join, or concatenate, two or more lists in Python.

.. code:: python

   list1 = ["a", "b", "c"]
   list2 = [1, 2, 3]

   list3 = list1 + list2
   print(list3)

Append list2 into list1:

.. code:: python

   list1 = ["a", "b" , "c"]
   list2 = [1, 2, 3]

   for x in list2:
   list1.append(x)

   print(list1)

Use the extend() method to add list2 at the end of list1:

.. code:: python

   list1 = ["a", "b" , "c"]
   list2 = [1, 2, 3]

   list1.extend(list2)
   print(list1)
