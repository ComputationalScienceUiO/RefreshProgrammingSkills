#!/usr/bin/env python
# coding: utf-8

# # Exercises

# ## Exercise 1 - Statistical Measures and Probability
# 
# You are given a list containing the total number of crimes per week over a number of weeks in The Republic.

# In[1]:


#The total number of crimes in a given week in The Reoublic
crimes = [31, 35, 49, 69, 103, 94, 46, 91, 68, 40, 98, 74, 40, 114, 48, 103, 88, 81, 65, 82, 64, 51, 91, 80, 90, 60, 77, 61, 46, 91, 96, 117, 35, 84, 92, 101, 69, 46, 27, 48, 109, 63, 77, 53, 61, 50, 74, 95, 114, 50, 89, 103, 73, 93, 103, 35, 108, 34, 64, 51, 95, 52, 97, 55, 96, 104, 96, 92, 86, 83, 51, 58, 33, 33, 65, 82, 48, 32, 108, 94, 100, 97, 34, 92, 80, 67, 60, 34, 114, 70, 52, 101, 80, 29, 48, 101, 35, 119, 86, 107, 44, 108, 94, 111, 39, 38, 81, 33, 111, 60, 75, 40, 100, 62, 55, 81, 51, 41, 76, 50, 77, 106, 105, 76, 50, 52, 80, 110, 101, 59, 39, 60, 67, 79, 31, 44, 28, 26, 71, 104, 99, 51, 34, 85, 92, 47, 110, 81, 69, 36, 64, 123, 114, 42, 125, 57, 94, 65, 41, 38, 32, 84, 80, 119, 51, 97, 61, 86, 112, 96, 78, 64, 69, 66, 90, 97, 93, 53, 60, 117, 84, 77, 100, 97, 94, 97, 45, 97, 33, 63, 32, 98, 91, 95, 107, 111, 89, 101, 84, 54, 81, 35, 36, 112, 74, 72, 64, 74, 81, 78, 47, 105, 57, 114, 75, 48, 36, 38, 34, 121, 76, 30, 51, 84, 116, 53, 33, 103, 96, 54, 98, 46, 88, 59, 100, 111, 79, 61, 70, 105, 97, 46, 99, 118, 39, 118, 62, 71, 31, 33, 35, 67, 77, 52, 55, 78, 88, 108, 34, 60]


# **a)** How many weeks does the dataset span?

# In[2]:


n = len(crimes)


# **b)** Selecting a week randomly, what is the probability that the number of crimes in it is:
# - more than or equal to 100?
# - less than or equal to 60?
# - between 60 and 100?

# In[3]:


crimesMore100 = 0
for crime in crimes:
    if crime >= 100:
        crimesMore100 += 1
print("The probability of there being more than or equal to 100 crimes is", round(crimesMore100/n, 3))

crimesLess60 = 0
for crime in crimes:
    if crime <= 60:
        crimesLess60 += 1
print("The probability of there being less than or equal to 60 crimes is", round(crimesLess60/n, 3))

print("The probability of there being between 60 and 100 crimes is", round(1 - crimesMore100/n - crimesLess60/n, 3))


# **c)** What is the expected value of the number of crimes in any given week?

# In[4]:


totalCrime = 0
for crime in crimes:
    totalCrime = totalCrime + crime
crimesEV = totalCrime / n

print("The expected number of crimes in any given week is", round(crimesEV, 2), "crimes.")


# **d)** Lawmakers have noticed that there is more crime reported in parts of the city with many officers on patrol. What are some possible explanations to this? (give at least two reasonable answers) What are some challanges in finding which explanation is correct?

# ```{toggle}
# It is possible that officers incite violence in the the part of the city they patrol. It might also be that officers patrol where the crime is to combat it. Another explanation is that officers record more crime places where there are more police to record it.
# ```

# **e)** What is the variance in the number of crimes in any given week?

# In[5]:


total = 0
for crime in crimes:
    squaredDifference = (crime - crimesEV)**2
    total = total + squaredDifference
crimesVar = total / (n - 1)

print("The variance in the number of crimes is", round(crimesVar,3))


# **f)** What is the standard deviation in the number of crimes in any given week?

# In[6]:


crimesStd = crimesVar**0.5

print("The standard deviation in the number of crimes is", round(crimesStd, 3))


# ## *Exercise 2 - In-Place Sorting Algorithm

# **Important note!** Refrain from using functions such as `sorted()` and `min()` to solve this exercise, as the point is implementing your own algorithms using loops, if-statements and lists.
# 
# In the previous exercise set you implemented a sorting algorithm that uses two lists to sort numbers. This uses a lot of space on the computer, and requires a many operations which change the size of lists. A better approach is using an algorithm that sorts a list without changing its size or using any other lists - an in-place sorting algorithm.
# 
# The sorting algorithm outlined here is an in-place sorting algorithm. (When testing this algorithm, it used 44.2 seconds to sort 30000 numbers. The algorithm from last week used 55.6 seconds. Both of these times are considered extremely slow.)
# 
# Here is a list of numbers:

# In[7]:


numbers = [5,1,6,3,2,6,1,1,4,78,4,12,12,6,23,12,4,3,34,2,1,43,7,7,2,3,4,214,5,1,2,7684,325,135,12353145,2,0,0,123,3,5,1,2,5,7,43,23,1]


# **a)** Find the smallest number in this list.

# In[8]:


n = len(numbers)

minimum = 0

for i in range(n):
    if numbers[i] < minimum:
        minimum = numbers[i]

print(minimum)


# **b)** Find the index of the smallest number in this list.

# In[9]:


n = len(numbers)

minIndex = 0

for i in range(n):
    if numbers[i] < numbers[minIndex]:
        minIndex = i

print(minIndex)


# **c)** Swap the smallest number in this list with the first element.

# In[10]:


temp = numbers[0]
numbers[0] = numbers[minIndex]
numbers[minIndex] = temp


# **d)** Now, find the smallest number in this list, beginning from the second element.

# In[11]:


n = n - 1

minIndex = 1

for i in range(1, n):
    if numbers[i] < numbers[minIndex]:
        minIndex = i

print(minIndex)


# **e)** Swap the number you found in e) with the second number in the list.

# In[12]:


temp = numbers[1]
numbers[1] = numbers[minIndex]
numbers[minIndex] = temp


# **f)** Sort the numbers in `numbers` in ascending order without creating another list. **Hint:** You will need two nested `for-loops`. One iterating `i` from 0 to `len(numbers)`, and one inside that one iterating `j` from `i` to `len(numbers)`. You can of course use other variable names instead of `i` and `j`.

# In[13]:


length = len(numbers)

for i in range(length):
    minIndex = i
    
    for j in range(i, length):
        if numbers[j] < numbers[minIndex]:
            minIndex = j
    
    temp = numbers[i]
    numbers[i] = numbers[minIndex]
    numbers[minIndex] = temp

print(numbers)

