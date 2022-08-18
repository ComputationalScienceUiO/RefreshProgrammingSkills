#!/usr/bin/env python
# coding: utf-8

# # Variables and Decisions
# 
# ## Learning Goals:
# 
# After this week, the student will be able to:
# - Declare variables
# - Do simple maths in Python
# - Write programs using *if* and *else* statements
# - Generate random numbers in python

# ## Introduction

# This course will teach you how to write code in the Python programming language. For our purposes code is instructions that computers can follow to complete tasks and solve problems for us.

# ## Hello world!

# To get started with coding, it is customary to write a "Hello world!" program, a program that prints the words "Hello world!" to the screen. In Python, this program looks like this:

# In[1]:


print("Hello world!")


# To write and run this program, you first need to open a code editor like jupyter lab (or Spyder or <a href="https://repl.it/languages/Python3">repl.it/languages/Python3</a>), then create a file with a suitable name(something like `hello.py` or `hello.ipynb` for notebooks) **in a folder you can find later**. Write `print("Hello world!")` in your file, and finally run your program.
# 
# The "Hello world" program contains two new and useful concepts:
# 
# The first is the string `"Hello world!"` inside the parentheses. In programming, strings are one of the basic data types used to store information. Strings are used to store text. To create one you need to surround the text you want to store with quotes like this: `"This is a string"`.
# 
# The second thing is the function `print()`. Whatever you put inside the parentheses will be written in the console. Nearly every single program in this course will include the `print()` function, we use it whenever we want our program to output some text. You will become familiar with many other functions during this course, and even make your own. Functions take some input inside the parentheses, and perform some action.

# ## Variables

# Variables are used to store numbers and text among other things. Variables are useful beacuse we often want to save useful information in our programs in order to access it later. You declare a variable by giving it a name and a value. Let's start by storing the number `5` in the variable `a`.

# In[2]:


a = 5


# Now the variable with the name `a` holds the value `5`. You can try running `print(a)` to see what happens.

# In[3]:


print(a)


# The number `5` was printed to the console, since printing the variable `a` prints its value and not its name. You can create as many variables as you want, and you can name them almost anything.
# 
# ```{admonition} Extra: Names you can't use for variables
# :class: toggle
# A variable name can't be a number, a special character or an important Python keyword like `print`. If a keyword is used for something else, it changes color in some editors, examples of such keywords are `if`, `else`, `sum` and `type`. Don't use these names for your variables, as you'll overwrite useful functions. Try naming a variable `print` and see what happens when you then try to print something.
# 
# ```
# 
# You can think of a variable as being an adress in your computer memory, and at that adress you store some value. When you want to access a value, you use its address to find it.
# 
# There are different **types** of variables that you should familiarize yourself with:

# ### Integers and Floats

# In Python, whole numbers are stored as **integers** and decimal numbers are stored as **floats**. They are declared in the same way though, so you often don't need to worry about the distinction. When doing calculations in Python, you can think of integers and floats as just being numbers. This is not the case in all other languages though.
# 
# To declare an integer, do as before and assign a whole number to a variable. To declare a float, assign a decimal number to a variable.

# In[4]:


thisNumber = 42
otherNumber = 2.718


# You can add, subtract, multiply and divide in Python like this

# In[5]:


total = 5 + 1
difference = 8 - 1
product = 13 * 2
quotient = 21 / 3


# To see the actual results we can print the value of the variables

# In[6]:


print(total)
print(difference)
print(product)
print(quotient)


# You can use variables as if they were numbers when doing calculations:

# In[7]:


print(product - total)


# There are other operations you can do in Python as well. Exponents are done with two multiplication signs. You can also take a square root by raising a number to the power of `0.5`.

# In[8]:


exponents = 2**3
print(exponents)
print(25**0.5)


# Parentheses work just like in regular maths.
# 
# **NOTE:** Remember to put an operator between numbers and parentheses though, or Python will treat the number like a function and your program won't run.

# In[9]:


parentheses = 5  * (2 + 3)
print(parentheses)


# This won't work: `parentheses = 5(2 + 3)`, neither will this: `result = thisNumber(2 + 4)`, because Python tries to use `thisNumber` as a function instead of a variable when you use parentheses like this.

# ---
# 
# ### In-Class Number Exercises

# **a)** Store the result of `1 + 1` in a variable and print it.
# 
# **b)** Store two different numbers in two variables. Add the variables together and print out the result.
# 
# **c)** Do calculations using all of the operators and print out the results.
# 
# ---

# ### Strings

# Let's declare some strings. Remember that you need to surround text with quotes when declaring strings. Single, double and triple quotes will all work.

# In[10]:


first = 'Stephen'
middle = "John"
last = '''Fry'''


# You can combine strings with `+`, and  make strings repeat by multiplying them with whole numbers, 

# In[11]:


print(first + middle +  last)
print(first * 5)
print(first + " " + middle + " " + last)


# Strings can contain almost any text, as long as you surround it with quotes.

# In[12]:


myText = "Spaces   numbers 2020 'other types of quotes'"
five = "5"
print(myText)
print(five * 2)


# A problem arises if your text contains quotation marks. `print("He cried: "Oh no"")` creates the string `"He cried: "` and the empty string `""`, and a mess in between that ruins the code. To avoid this problem, python uses the escape character `\` - placing this escape character before a special character (like `\n`, which creates a linebreak) renders it a normal character in the string: `print("He cried: \"Oh no\"")`. You could also use a different type of quotation marks on the outside: `print('He cried: "Oh no"')`.
# 
# A simple way of printing strings and numbers together is to use a comma between them.

# In[13]:


print("The best number is", 43 * 3, "without a doubt")


# ### Better printing:

# A much better way of adding numbers or variables in the middle of text is to use f-strings (the f is for "format"). Put an f in front of the quotation marks, and use curly brackets where you want to add numbers or variables.

# In[14]:


print(f"The best number is {43 * 3} without a doubt")


# In[15]:


first = "James"
last = "Bond"
print(f"My name is {last}, {first} {last}.")


# You can also use f-strings to round numbers, which can be useful when trying to make results more readable. To round a number to two decimals, add `:.2f` at the end of the curly bracket with a number. You can change the `2` to include more or fewer decimals. By adding `:.0f` after a number you can add it to the string without any decimals.

# In[16]:


print(f"The best number is {22/7} without a doubt, or maybe {22/7:.2f}, or maybe even {22/7:.0f}")


# If you want to print the name and value of a variable, it can be done like this:

# In[17]:


number = 42
print(f"{number = }")


# ---
# 
# ### In-Class String Exercises

# **a)** Store your name in a string. Using this string, make the computer print out that you're doing a good job.
# 
# **b)** Store you age as an integer. Using this integer, print out that it is your age.
# 
# **c)** Store the value `5.555` in a variable called `myFloat`. Using string formatting, `print` the value of `myFloat` with one decimal.

# ---

# ### Changing a variable

# If you assign two different values to a variable with the same name, the last value is the one that will be stored.

# In[18]:


b = "Text"
b = 40 #b now stores an integer, and not the string "Text"
print(b)


# You can assign the value of one variable to another.

# In[19]:


a = 5
b = a #Now b = 5
a = 17 #This changes a, but not b
print(b)


# ### Comments

# To write good code you should write good comments when needed. You comment your code by writing `#` and then your comment anywhere in your code. Comments are ignored by the computer when you run your code. Commenting your code to clarify what it does to yourself and others who might read it is a good practice. You should only add comments when it is needed for clarity, otherwise you only end up making the code less readable.

# In[20]:


myName = "Ola Nordmann" #This is a comment
myNumber = 6224

print(myName * 2, myNumber * 2) #The first multiplication makes the string repeat itself, the second doubles the number stored in myNumber

#print(myName + myNumber) this line has been "commented out", so the code here won't be run. If you were you run this code you would get an error anyway, since you can't add a string and integer


# ---
# 
# ### In-Class Variable Changing Exercises

# **a)** Define a variable `myNum` with the value `10` and a variable `yourNum` with the value `42`. Use a third variable `temp` to switch the values of `myNum` and `yourNum`.
# 
# **b)** What would the output of this code be?
# 
#     a = 10
#     b = 7
#     
#     a = b
#     b = a + 5
#     #b = a + b
#     
#     print(a)
#     print(b)
#     
# ---

# ## Decisions

# We often want our program to do different things depending on the state of the program. Much like how we might want to bet different amounts in poker depending on the quality of our hand.
# 
# To make our programs make decisions in Python, we use `if` and `else` statements.
# 
# When the computer reaches an `if` statement, it checks whether the logical statement is true or not. If it is, the code below the `if` statement that is **indented** is run. If not, the indented code is skipped. Indented code is code with blank space to its left. We normally use the "tab" key to indent code.

# In[21]:


myNumber = 5

if myNumber > 3:
    print("Hello!")

if myNumber > 8:
    print("Goodbye!")


# We can expand this program with an `else` statement. The indented code under the `else` statement is run whenever the `if` statement above "fails".

# In[22]:


myNumber = 5

if myNumber > 8:
    print("The number was bigger than 8")
else:
    print("The number was not bigger than 8")


# We can also use strings in the logical statements in the `if` statements:

# In[23]:


name = "John"

if name == "Kant":
    print("I'm sorry, but I Kant remember your name, what was it again?")
else:
    print(f"Hello {name}.")


# We can also put `if` statement inside other `if` or `else` statements. These nested `if` statements work just like the ones we just looked at, but the program reaches them only if the outside `if` statement "succeeded".

# In[24]:


name = "John"
age = 31

if name == "Kant":
    if age == 297:
        print("Guten tag mein mann!")
    else:
        print("I'm sorry, but I Kant remember your name, what was it again?")
else:
    print(f"Hello {name}")


# ---
# 
# ### In-Class Decisions Exercises

# **a)** Write a program that checks whether an integer variable is greater than 10.
# 
# **b)** Write a program which greets children with the phrase "Hey kid", and adults by their name.
# 
# **c)** Write a program that uses a nested `if` statement.
# 
# ---

# ## Elif statements and larger decision blocks

# We can expand this program again by combining an `if` statement and an `else` statement into an `elif` statement. The `elif` statement is run when an `if` statement right above it fails.
# 
# When you have multiple decisions chained together like this, the final `else` only "succeeds" when all prevous `ifs` and `elifs` failed or were skipped. Only an `if` can start such a chain, and when you reach an `else` the chain is stopped.
# 
# The trolley problem is a thought experiment where a trolley is about to run over five people on the main track, but you can divert it to a side track where it will run over only one person.
# 
# Let's write a program that chooses what action to take depending on which action saves the most lives.

# In[25]:


mainTrack = 5
sideTrack = 1

if mainTrack > sideTrack:
    print("Change the tracks!")
elif mainTrack == sideTrack:
    print("I honestly don't care what you do.")
else:
    print("Don't change the tracks!")


# We can also put `if` statement inside other `if` or `else` statements. These nested `if` statements work just like the ones we just looked at, but the program reaches them only if the outside `if` statement "succeeded".
# 
# Let's write a program which does the same as last time, only now it can also choose to blow up the trolley if that saves the most lives.

# In[26]:


mainTrack = 5
sideTrack = 8
passengers = 4

if mainTrack > sideTrack:
    if sideTrack > passengers:
        print("Blow up the trolley!")
    else:
        print("Switch the tracks!")
        
elif mainTrack == sideTrack == passengers:
    print("I honestly don't care what you do.")
    
else:
    if mainTrack > passengers:
        print("Blow up the trolley!")
    else:
        print("Don't switch the tracks!")


# **1.** First the variables `mainTrack`, `sideTrack` and `passengers` are declared
# 
# **2.** Then the program reaches the first `if` statement. `mainTrack` is not greater than `sideTrack`, so the program skips the indented code under the first `if` statement.
# 
# **3.** Then it reaches an `elif` statement. `mainTrack`, `sideTrack` and `passengers` are not all equal, so this `elif` statement "fails". The indented code is skipped and the program reaches an `else` sentence.
# 
# **4.** Everything on the level of this `else` statement failed, so the indented code under it is run.
# 
# **5.** There it reaches an `if` statement. `mainTrack` is greater than `passengers`, so the `if` statement succeeds and the indented code is run. "Blow up the trolley!" is printed.
# 
# **6.** Finally, the last `else` is reached and since the previous `if` succeeded, it is skipped. The program has now reached the end.
# 
# This example brings up an important question when writing programs that make decisions in the real world. Should a program choose whether a self driving car should sacrifice a passenger or a pedestrian if it comes down to it during a potential collision? And if so, what should it choose? Should this decision be made by the car manufacturers?

# ### Logical statements and booleans

# We often compare numbers in `if` and `elif` statements. These are the five different logical operators you can use to compare numbers:
# 
# Let `a = 5`
# 
# - `a < 5` returns False
# - `a > 5` returns False
# - `a == 5` returns True *(equal, you NEED two equal signs)*
# - `a <= 5` returns True *(less than or equal)*
# - `a >= 5` returns True
# - `a != 5` returns False *(not equal)*

# You can store the value of these logical statemens in variables called booleans. Booleans can hold the values `True` or `False` and can be used for logical operations. Python uses the `and`, `or` and `not` keywords for logical operations.

# In[27]:


sunny = True
ownSunscreen = False

if sunny and not ownSunscreen:
    print("Go buy some sunscreen!")


# - `True and True -> True`
# - `True or True -> True`
# - `True or False -> True`
# - `not True -> False`
# - `not False -> True`
# - `True and False -> False`
# - `False and False -> False`
# - `False or False -> False`

# ---
# 
# ### In-Class Decisions With `elif` Exercises

# **a)** Write a program that is nice to people called "Alice" and rude to people called "Bob", while other people are given a standard greeting.
# 
# **b)** Write a program that makes a decision in the trolley problem, such that the most people are killed.
# 
# **c)** Try comparing two strings using the `<` operator. Write a program that compares two words and prints out the one which comes first alphabetically (only use lower case letters).
# 
# ---

# ## Random number generation

# By using built-in functionality in your computer and clever maths, Python can generate psuedorandom numbers. They're not actually random numbers, since they're generated from a starting number using a sequence of equations. But psuedorandom numbers are still distributed like random numbers, which is what we care about(therefore, we will just be calling them random numbers from now on). To generate them we need to `import` the `randint()` function like this:

# In[28]:


from random import randint


# Python includes a lot of functionality right out of the box, but we often need even more functionality. To access this functionality, we `import` modules. In this case, we imported the `randint` function from the `random` module so that we can generate random numbers. Now we can use this function freely in our program, much like how we would use the `print()` function.
# 
# The `randint()` function takes two arguments, a starting number and an ending number. The function then returns a random between the starting number and the ending number. What that means is that `randint(1, 6)` can return any of the numbers 1, 2, 3, 4, 5 or 6, with equal probability.
# 
# Using this we can simulate the throw of a die! Write these lines of code and run it multiple times to see what happens.

# In[29]:


dice = randint(1,6) #generates a random number between 1 and 6, like a die
print(dice)


# We can also simulate a cointoss like this:

# In[30]:


coin = randint(0, 1)

if coin == 0:
    print("Heads!")
else:
    print("Tails!")


# ---

# ### In-Class Random number exercises

# The variable `dice` holds a random value from 1 to 6, like a diceroll.
# 
# **a)** What is the probability that A will be printed?
# 
# **b)** What is the probability that B will be printed?
# 
# **c)** What is the probability that B will be printed given that A has been printed?

# In[31]:


dice = randint(1,6)

if dice > 3:
    print("A")

if dice == 6:
    print("B")


# **d)** Does this change the behaviour of the code?

# In[32]:


dice = randint(1,6)

if dice > 3:
    print("A")
    if dice == 6:
        print("B")


# ---
