#!/usr/bin/env python
# coding: utf-8

# # Exercises

# If you ever get really stuck on an exercise, skip it and **ask for help!**

# ## Exercise 1 - Lists

# **a)** Create a list with five names. Use a loop to print greetings including each name.

# In[1]:


names = ["Nils", "Olav", "Ivar", "Levi", "Kristian"]

n = len(names)
i = 0
while i < n:
    name = names[i]
    print("Good day " + name + "!")
    i = i + 1


# **b)** Create a list with ten integers.
# - Change the first element to be equal to the fifth
# - Print the third element
# - Add 5 to all elements (while loop)
# - Swap the first and last elements
# - Remove the second element of the list using `removedElement = myList.pop(index)`. We won't use `pop()` much in this course, but we introduce it here as it will be used in exercise 6.

# In[2]:


numbers = [4, 13, 1450, 201, 14, 1, 0, 4, 12, 42]

numbers[0] = numbers[4]
print(numbers[2])

n = len(numbers)
i = 0
while i < n:
    numbers[i] = numbers[i] + 5
    i = i + 1
    
temp = numbers[0]
numbers[0] = numbers[n - 1]
numbers[n - 1] = temp

removedElement = numbers.pop(1)

print(numbers)


# ## Exercise 2- Loops

# **a)** Write a program that prints all even numbers from 0 to 20.

# In[3]:


i = 0
while i < 21:
    print(i)
    i = i + 2


# **b)** Print the 7 times table.

# In[4]:


for i in range(0, 71, 7):
    print(i)


# **c)** Create a list with the numbers $\frac{1}{1}$, $\frac{1}{2^2}$, $\frac{1}{3^2}$, $\frac{1}{4^2}$ and so on, with 1000000 elements.

# In[5]:


nums = []

for i in range(1, 1000001):
    nums.append(1/i**2)


# **d)** Find the sum of every element in your list from **c)**, multiply it by 6, and take its square root. Is there anything special about the result?

# In[6]:


total = 0

for i in nums:
    total = total + i
    
total = (total * 6)**0.5

print(total) # It's an approximation for pi!


# **e)** Write a program that finds the sum of all odd numbers from 1 to 1001. How can you test that your program works?

# In[7]:


total = 0
for i in range(1, 1002, 2):
    total += i
    
print(total) # You can test your program by making sure it works for cases you can check by hand like the odd numbers up to 7 and 11


# ***f)** Create a list with 10 numbers. Reverse it without using any built-in functions or tricks (like `myList.reverse()` or `myList = myList[::-1]`).

# In[8]:


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

n = len(numbers)

for i in range(int(n/2)): # looping halfway through the list
    temp = numbers[i]
    numbers[i] = numbers[n-1-i]
    numbers[n-1-i] = temp # swapping the first and last elements and doing the same moving inwards

print(numbers)


# ## *Exercise 3 - Sorting Algorithm

# **Important note!** Refrain from using functions such as `sorted()` and `min()` to solve this exercise, as the point is implementing your own algorithms using loops, if-statements and lists. Feel free to use `len()`, `pop()` (removes element) and `append()`. In all other cases you *really* should use functions like `sorted()` and `min()` though!
# 
# Sorting algorithms are some of the most used algorithms in the world. When you make an online search, the search engine sorts the results after relevance. Shopping sites let you choose between different criteria for sorting their products. And of course, Netflix sorts movies and shows after what is most likely to keep you subscribed.
# 
# The simplest case however, is sorting a list of numbers. There are many different ways of sorting numbers, each one with its pros and cons. The sorting algorithm outlined here is slow and uses a lot of space compared to more advanced sorting algorithms. It is however, a good exercise in algorithmic thinking.
# 
# Here is a list of numbers:

# In[9]:


numbers = [5,1,6,3,2,6,1,1,4,78,4,12,12,6,23,12,4,3,34,2,1,43,7,7,2,3,4,214,5,1,2,7684,325,135,12353145,2,0,0,123,3,5,1,2,5,7,43,23,1]


# **a)** Find the smallest number in this list.

# In[10]:


small = numbers[0]

length = len(numbers)

i = 0
while i < length:
    if numbers[i] < small:
        small = numbers[i]
    i = i + 1
    
print(small)


# **b)** Find the index of the smallest number in this list.

# In[11]:


small = numbers[0]
smallIndex = 0

length = len(numbers)

i = 0
while i < length:
    if numbers[i] < small:
        small = numbers[i]
        smallIndex = i
    i = i + 1
    
print(smallIndex)


# **c)** Remove the smallest number from this list using `smallest = numbers.pop(index)`.

# In[12]:


smallest = numbers.pop(smallIndex)


# **d)** Create a new list `sortedNumbers` and add the smallest element from `numbers` to it using `sortedNumbers.append(smallest)`

# In[13]:


sortedNumbers = []
sortedNumbers.append(smallest)


# **e)** Fill `sortedNumbers` with all of the numbers from `numbers` in ascending order. **Hint:** Make the code from **b)**, **c)** and **d)** run `len(numbers)` times.

# In[14]:


length = len(numbers)

i = 0
while i < length: #Running the code from b, c and d len(numbers) times
    small = numbers[0]
    smallIndex = 0
    newLength = len(numbers) #The search for the new smallest number now goes over fewer elements
    j = 0
    while j < newLength:
        if numbers[j] < small:
            small = numbers[j]
            smallIndex = j
        j = j + 1
    smallest = numbers.pop(smallIndex)
    sortedNumbers.append(smallest) #.append() adds an element to the end of the list, so this ends up sorting all the numbers
    
    i = i + 1

print(sortedNumbers)

