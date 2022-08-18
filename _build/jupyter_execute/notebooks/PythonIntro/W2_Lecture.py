#!/usr/bin/env python
# coding: utf-8

# # Lists and Loops
# 
# ## Learning Goals
# 
# After this week, the student will be able to:
# - Write programs using lists
# - Write programs using for-loops
# - Access and manipulate relevant features of strings

# ## Lists

# Lists are used for storing many variables in a compact way. You make one using brackets.

# In[5]:


mylist = [10, "Stephen", 40, 99, False, "Fry"]
print(mylist)


# You can access specific elements in a list by writing the name of the list next to brackets with an index inside them.

# In[6]:


print(mylist[0])


# The first element in a list has the index 0, the second element has the index 1 and so on.

# In[53]:


words = ["first", "second", "third", "fourth", "fifth", "sixth"]
print(words[0])
print(words[2])
print(words[1:5:2]) # Extra: Slicing! This gives elements from start:stop:step. In this case the elements with index 1 and 3.


# While a variable can be though of like an address in computer memory with a specific value, a list is more like a parking lot. The list also has an address, but to get or store a value you need to specify a parking spot.

# You can add elements to the end of a list by using the method `.append()`. Methods are like functions, only they need to be used on something. The `.append()` method for instance, needs to be used on a list.

# In[33]:


words.append("fifth")
words.append(30)
print(words)


# You can change the elements of a list by using indexes.

# In[34]:


words[1] = "something else"
print(words)


# You can find the length of a list by using the function `len()`.

# In[35]:


print(len(words))


# The `in` keyword checks if a value appears in a list and returns `True` or `False`.

# In[37]:


if "third" in words:
    print("The string exists in the list")


# ---
# 
# ### In-Class Lists exercises

# **a)** Create a list filled with the names of your favorite movies and shows.
# - Use `.append()` to add an element to it.
# - Print the second element of the list
# - Change the second element of the list to "Better Call Saul"
# - Print the second element of the list
# - Print the length of your list
# ---

# ## For loops

# One of the biggest strengths of computers is their ability to do many small operations over and over. Complex operations like performing statistical analysis, translating millions of sentences and simulating the spread of a disease cannot be done in one fell swoop, they must be broken into smaller parts which together give the correct result.
# 
# The simplest way of performing many small operations with code is using loops. Loops are used to run code over and over again. In Python there are two types of loops, while-loops and for-loops. We will focus on using for-loops, since they are more useful for our purposes.
# 
# If we wish to print "Hello World!" three times it can be done like this:

# In[10]:


for i in range(3):
    print("Hello World!")


# `i` is the iteration variable. It can be used inside the loop.

# In[2]:


for i in range(3):
    print(f"The iteration variable has the value {i}")


# The `range()` function determines how many times the `for` loop is run, and which values the iteration variable `i` will have for each iteration. `range(3)` makes the code inside the loop run once for each of the `i` values `0` -> `1` -> `2`. `range(100)` would make the code inside the loop run once for each of the values `0` -> `1` -> ... -> `98` -> `99` (100 times in total).
# 
# The `range()` function can also be used in a slightly different way. You can give it a number to start from, a number where to stop and a step length. `range(2, 12, 2)` would make the code inside the loop run for each of the `i` values `2` -> `4` -> `6` -> `8` -> `10`. The order of the arguments are `range(start, stop before, step)`. The iteration variable can have any name.

# In[16]:


total = 0 # declared BEFORE the loop!

for number in range(2, 12, 2):
    print(number)
    
    total += number # updating INSIDE the loop
    
print(f"The total is {total}") # printing AFTER the loop


# ---
# 
# ### In-Class For-loop Exercises
# 
# **a)** Write a program which prints "Karma" 5 times. Then "Chameleon" 1 time. Then "You come and go" 2 times. Use loops for **all** repeated printing!
# 
# **b)** Using a for loop with a start, stop and step lenght, calculate the sum of all odd numbers from 1 to and including 101. To make sure you have the right approach, you can try from 1 to 7 first.
# 
# **c)** Were both of these exercises a good use of loops?
# 
# ---

# ### Iterating through a list
# 
# A very useful use-case for a `for` loop is iterating through a list. Instead of making the iteration variable the numbers that the `range()` function gives us, we can make it go through the elements of a list using the `in` keyword.

# In[14]:


myList = [5, 30, 7, 2]

for element in myList:
    print(element)


# Just like how you can put multiple `if` sentences inside eachother, you can put a `for` loop inside another `for` loop.

# In[13]:


for i in range(2): #i is 0 then 1
    for j in range(3): #j is 0 then 1 then 2
        print(f"i = {i} -- j = {j}")


# ---
# 
# ### In-Class Looping Through Lists Exercises
# 
# **a)** Create a list of five names, then iterate through it printing out each name with a greeting.
# 
# **b)** Extend the previous program so that the greeting is different if the name is your name.
# 
# **c)** Create a list with five numbers, then calculate the total of all the numbers.
# 
# **d)** Create a list with five numbers, then calculate the average.
# 
# ---

# ## Advanced List Indexing

# There are a few different ways to access elements in a list. You are already familiar with using an index inside of brackets.

# In[1]:


myList = [1, 2, 3, 4, 5, 6, 7]
print(myList[3])


# You can also use negative indexes. `-1` gives to the last element, `-2` the second to last and so on.

# In[2]:


print(myList[-1])
print(myList[-2])


# You can also use what is called slicing to get only some of the elements of the list. Slicing works like this: `myList[from:to]` returns all of the elements from index `from` to index `to`, not including the element at index `to`. You can also slice with `myList[to:from:step]`, which does the same thing, but only includes every `step` elements.

# In[3]:


print(myList[1:6])
print(myList[1:6:2])

