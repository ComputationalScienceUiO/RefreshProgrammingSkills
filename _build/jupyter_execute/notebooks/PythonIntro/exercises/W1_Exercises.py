#!/usr/bin/env python
# coding: utf-8

# # Exercises

# If you ever get really stuck on an exercise, skip it and **ask for help!**

# ## Exercise 1 - Variables

# **a)** What is a variable? Why do you think they are called variables?

# ```{toggle}
# A variable is a storage adress associated with a variable name. Some value is stored at the adress. They might be called variables because their values can vary during the execution of a program.
# ```

# **b)** Define two integers and print their sum.

# In[1]:


a = 50
b = 21414
print(a + b)


# **c)** Define two strings, add them together (`+`), and print the result.

# In[2]:


first = "Bob"
last = " Ross"
print(first + last)


# **d)** Let `a`, `b` and `c` be declared like in the code below. Use a fourth variable to swap the values of `a` and `b`, and then `b` and `c`.

# In[3]:


a = 1
b = 2
c = 3

temp = a
a = b
b = temp

temp = b
b = c
c = temp


# **e)** What will this code output?
# 
#     a = 3
#     b = a
#     a = 5
#     print(b)

# ```{toggle}
# It will output `3`, as b was defined to be the value of `a` when `a` was `3`.
# ```

# **f)** What is the difference between `3`, `3.0`, `'3'`, `'''3'''` and `"3"`?

# ```{toggle}
# In order, their type is: integer, float, string, string, string.
# ```

# **g)** What variable type should be used to store:
# - Whether Wednesday's weather will water wallflowers
# - The number Wednesdays on which it has rained before
# - The probability of it raining on Wednesday
# - A description of Wednesday's weather

# ```{toggle}
# - Whether Wednesday's weather will water wallflowers - boolean
# - The number Wednesdays on which it has rained before - integer
# - The probability of it raining on Wednesday - float
# - A description of Wednesday's weather - string
# ```

# **h)** What happens when you try to print the following:
# - `1/0`
# - `variableName(40)`
# - `"Ola" + 5`
# - `"Ola", 5`

# ```{toggle}
# - `1/0` - You will get a zero division error
# - `variableName(40)` - You will get an error as you are trying to call a function which is undefined. Or if variableName is a defined variable, you will get an error from trying to call a variable as a function.
# - `"Ola" + 5` - You will get an error as you cannot add together strings and integer
# - `"Ola", 5` - You will print "Ola 5"
# ```

# ## Exercise 2 - Decisions

# **a)** Write a program that prints whether a number is larger than 10.

# In[4]:


number = 10

if number > 10:
    print("The number is larger than 10")
else:
    print("The number is not larger than 10")


# **b)** Write a program that declares two integers, `smallest` and `largest`. Make it so that if `smallest` is the largest number, the values are swapped.

# In[5]:


smallest = 40
largest = 12

if largest < smallest:
    temp = smallest
    smallest = largest
    largest = temp


# **c)** Write a program that grants any loan under 1 million to anyone between the ages of 18 and 80.

# In[6]:


age = 33
loanAmount = 999999

if age > 18 and age < 80:
    if loanAmount < 1000000:
        print("Yes")
    else:
        print("No")
else:
    print("No")


# **d)** Write a program that grants a loan randomly, with different probabilites depending on some factor like gender, age or loan amount. (using `randint()`)

# In[7]:


from random import randint

age = 33
loanAmount = 999999

if age > 33: #50% of people older than 33 are given loans under 100k
    if randint(1, 2) == 1 and loanAmount < 100000:
        print("Yes")
    else:
        print("No")
else: #20% of people 33 or under are given loans under 100k
    if randint(1, 5) == 1 and loanAmount < 100000:
        print("Yes")
    else:
        print("No")


# ## Exercise 3 - Random number generation

# **a)** Write a program that prints a random whole number from 0 to 50.

# In[8]:


num = randint(0, 50)
print(num)


# **b)** Write a program that prints a random even number from 0 to 100.

# In[9]:


evenNum = randint(0, 50) * 2
print(evenNum)


# **c)** Write a program that prints out "Heads" 49% of the time, "Tails" 49% of the time, and "Standing" 2% of the time.

# In[10]:


result = randint(1,100)

if result <= 49: #1 to 49 is 49%
    print("Heads")
elif result <= 98: #50 to 98 is 49% 
    print("Tails")
else: #99 and 100 is 2%
    print("Standing")


# **d)** Write a program that generates 5 random coin tosses (50% heads, 50% tails), and prints out the total number of heads.

# In[11]:


heads = 0
heads = heads + randint(0,1)
heads = heads + randint(0,1)
heads = heads + randint(0,1)
heads = heads + randint(0,1)
heads = heads + randint(0,1)

print("The total number of heads is", heads)


# **e)** Write a program that throws an error 50% of the time.

# In[12]:


coin = randint(0,1)

if coin == 0:
    print(1/0)
else:
    print("Phew!")

