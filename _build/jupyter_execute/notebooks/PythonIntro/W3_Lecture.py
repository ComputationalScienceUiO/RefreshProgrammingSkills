#!/usr/bin/env python
# coding: utf-8

# # Data Processing and Statistics

# ## Learning Goals:
# 
# After this week, the student will be able to:
# - Read and write files using Python
# - Calculate the expected value, variance and standard deviation of a set of numbers
# - Write programs using user input
# - Solve decision problems using expected values

# ## Reading and Writing Text Files 

# The standard way to access text files in Python is using the built-in function `open`. This function takes two arguments; the first argument is the name of the file, and the second argument specifies whether the file shall be read or written to. If the second arguments is `"r"`, it means we want to open the file for reading, whereas giving `"w"` means we want to open the file for writing. If some text is to be appended to the contents of an already existing file, we can use `"a"` as an argument. Giving `"w+"` as the second argument to `open` will tell the machine that the file is to be both written to and read. The default option for the second arguments is `"r"`, so if we don't provide a second argument to `open`, Python will assume that we want to be in read-mode.  

# ### Writing Text to a File

# Writing to a text file in Python can be done by using the built-in function `open`, and giving the string `"w"` as the second argument to the `open`-function. In the following example, a file with the name `textfile.txt` is created. The file name extension `.txt` is customary for text files, but we could in principle give the file any extension we want. 

# In[1]:


ofile = open("textfile.txt", "w")


# The command above creates a file on the computer, called `textfile.txt`, and creates a `File` object that we call `ofile`. `File` objects is something we use in Python to handle files. We want to proceed by filling this file with some information. Below we fill the file with the sentence "This is line number" and then the number of the line. This is done by creating a string constaining the quote, and writing this string to the file `textfile.txt` through the `write`-function on the `File`-object, as shown below. 

# In[2]:


for i in range(10):
    ofile.write(f"This is line number {i+1:.0f}\n")


# When we are finished writing to the file, we close it using the `close`-function on the `File` object. 

# In[3]:


ofile.close()


# This makes sure that everything we wanted to write to the file is actually written there, and it can prevent slowdown when very large files which are opened are no longer needed. This is similar to ejecting a USB stick in the operating system before actually detaching it from the computer physically. 

# ### Reading Text from a File

# If we want to analyze texts, we usually want to read files, rather than writing them. To read files, we use the built-in Python function `open`, with `"r"` as the second argument, to create a `File`-object that reads a particular file. We can use the `read`-function on the `File`-object to get the entire contents of the file returned as a single string. This is shown in the example below, which opens the file that we just created in the last section.

# In[4]:


ifile = open("textfile.txt", "r")
content = ifile.read()
print(content)

ifile.close()


# If you only want to read a single line, you can use the `readline` function.

# In[5]:


ifile = open("textfile.txt", "r")
content = ifile.readline()
print(content)


# The `File`-object reads from the beginning, and cannot re-read something it has read.

# In[6]:


print(ifile.readline())
print(ifile.read())
print("The file has reached the end, so nothing will be printed below")
print(ifile.read())

ifile.close()


# You can also read the entire file at once and make each line an element in a list:

# In[7]:


ifile = open("textfile.txt", "r")
content = ifile.readlines()
print(content)
ifile.close()


# When we ask Python to open the file `textfile.txt`, Python looks for this file in the same folder as where we are running Python from. We typically run from the same path as where the `.py` file is saved. Therefore, we usually want to have the text file in the same folder as the Python program reading it. If your text file is close to your python script, but not in the same folder, you can use the relative path to the file to open it. For instance: `Poems/textfile.txt`.
# 
# If the text file is somewhere completely different, you can tell the computer explicitly where to look for it. If the file `"textfile.txt"` lies in the `Documents`-folder on your computer, you can (on unix-based operating systems) use the absolute path `"/Users/username/Documents/textfile.txt"`, as the first argument of the `open`-function. The username is the name of the user at the computer you are using.

# ---
# ### In-class exercises 
# 
# **a)** Create and write to a file.
# 
# **b)** Read and print the contents of the file.
# 
# ---

# ## Working with data

# We have now learned how to read text from a file into python. Next we need to do something with it. Say we have a file with headers and a bunch of numbers:
# 
# ```
# Age    Height
# 72     160
# 34     181
# 18     109
# 34     172
# 19     194
# 37     190
# 21     100
# 88     135
# 14     197
# 19     150
# ```
# 
# How you read such a file depends on how many columns of data there is and how the numbers are seperated. Numbers are often seperated by commas, in the format called `.csv` (comma seperated values). In this case the numbers are seperated by spaces, so we need to account for that:

# In[8]:


ifile = open("data.txt", "r")
ifile.readline() # skipping the first line to skip headers

ages = []
heights = []

for line in ifile.readlines(): # looping through all lines of text
    nums = line.split() # splitting the line by blankspaces
    ages.append(int(nums[0])) # turning the first element of the line into an integer and adding it to ages
    heights.append(int(nums[1]))
ifile.close()

print(ages)
print(heights)


# This is a lot of code for very inflexible file reading! What if the file had 40 columns? You would have to create a list for every column and do the correct type conversion for each type of data.
# 
# When reading any data in python you should use the library **pandas**. Learn to use it! See the sidebar on this website for some material on how to use it.

# ### Calculating Expected Value
# 
# One of the things we can infer from looking at data is the expected value of an event, in this case the expected age of death of a newborn.
# 
# To find the expected value of an event from data, we take the average of the values observed.

# In[9]:


ages = [2, 11, 23, 64, 89, 91, 10, 20, 95, 8, 36, 100, 84, 62, 6, 16, 7, 89, 19, 62, 19, 27, 94, 80, 4, 21, 68, 97, 64, 72]

n = len(ages) #The number of datapoints

total = 0 #We tally up the total to calculate the average at the end

for age in ages:
    total = total + age
    
EV = total / n

print(f"The expected age is {EV:.1f} years") #round rounds a number to a specified number of decimals, here 1


# The data shows that the life expectancy of this population is 48 years. This does not mean that a person will most likely become 48 years old however, only that the average age of many people will be around 48 years. If you look at the data, you can actually see that not a single person died in their 40's or 50's, showing that expected value and most likely value are two very different things.
# 
# This behaviour is somewhat typical of life expectancy data. Due to high child mortality rates in developing countries, the life expectancy might be very low, while adults becoming old is still quite common. You see this in Sierra Leone where the life expectancy at birth is 52.5 years, while at 5 years old it is 59.7, a much larger increase than you see in Norway, where it goes from 80.6 to 80.8. (Source: <a href="https://www.worldlifeexpectancy.com/country-health-profile/sierra-leone">worldlifeexpectancy.com</a>)
# 
# Keep in mind that we only found the expected value of our sample. The expected value of the actual population can be slightly different. The larger the sample, the more certain we can be that the values we calculate are actually close to the actual values for the population. 

# ---
# 
# ### In-Class Expected Value Exercises
# 
# Alice and Bob both offer you what they call a great oppurtunity to get rich quick. They say that by giving them 10 dollars, you have a good chance of making large gains. Below are example gains from people taking them up on their offers in the past:

# In[10]:


alice = [-10, -10, -10, -10, -10, -10, -10, 1000, -10]
bob = [-10, 200, -10, 200, -10, 200, 200, 50, 50]


# **a)** Whose offer has the highest expected gains?
# 
# **b)** How would you describe what you can expect when taking them up on their offer? Does anything but the expected value matter?
# 
# **c)** Calculate the average word length of Pride and Prejudice. Calculate the average word length of The Three Little Pigs text. The text files can be found on the course website under "Extra Resources".

# ---

# ### Calculating Variance and Standard Deviation
# 
# To describe this large spread in ages of death we can calculate the variance of the data. To do this we take the average of the squared differences from the expected value(not as complicated as it sounds!). We could have just looked at the average difference from the expected value, but it is often of more interest to make large deviations from the expected value result in very large changes in the variance.
# 
# When the data we have is only a sample of the total population, the variance tends to be too small compared to the actual variance of the total population. To account for this, we divide by $n - 1$ instead of $n$ when taking the average. The standard deviation is the square root of the variance, and is the value most often used to describe the amount of dispersion in the data.

# ```{figure} assets/VarianceFigure.png
# ---
# name: my-figure
# ---
# Example of calculation of sample variance and standard deviation
# ```

# In[11]:


total = 0

for age in ages:
    squaredDifference = (age - EV)**2
    total = total + squaredDifference
    
variance = total / (n - 1)

print(f"The variance is {variance:.1f} years squared")


# This number is very large and not very intuitive (It has units years squared!). The standard deviation is the square root of the variance, and is often much more useful.

# In[12]:


std = variance**0.5

print(f"The standard deviation is {std:.1f} years")


# This number describes how spread out our data is. If all of the ages were in the range 60-80, the standard deviation would be much smaller.

# ---
# 
# ### In-Class Variance and Standard Deviation Exercises
# 
# 
# You have contracted a deadly disease and have 12 months left to live. There is an operation which has a chance to greatly increase your remaining time here on earth.
# 
# This is how long people in your exact position lived after taking the operation:

# In[13]:


monthsLeft = [0, 30, 2, 0 , 1, 0, 412, 0, 2, 1, 0, 5, 0, 12, 44, 0, 0, 0, 5, 0, 1, 0, 0, 0, 203, 40, 6, 0, 0, 3, 2, 0, 2, 0, 0, 5]


# **a)** Calculate the expected value of remaining months if you take the operation.
# - Should you take the operation?
# 
# **b)** Calculate the sample variance of the remaining months if you take the operation.
# 
# **c)** Calculate the standard deviation of the remaining months if you take the operation.
# - Is the operation risky?
# 
# **d)** How large a percentage died within 0 months of taking the operation?
# 
# **e)** Calculate the variance of the expected word length of a text.
# 
# ---

# ## User Input - Communicating with your program

# Python has a built in funtion called `input()` which prints a message to the terminal and then returns whatever the user writes in the terminal as a string.

# In[14]:


name = input("What is your name?: ")
print("Hello " + name)


# If you want to input a number and then use it for calculations, you need to turn the string into an integer or float first.

# ### Type conversion

# You can turn one type of variable into another type like this:

# In[15]:


myString = "15"
myInt = int(myString) #The string has to contain a whole number! "15.2" would not work
myString2 = str(myInt)
myFloat = float(myInt)
myFloat2 = float(myString) #The string has to contain only a number! "Hey 24.4" would not work, "24.4" would


# Turning a float into an integer can often be useful, because some functions will not accept a float as an input, even if it is a whole number.
# 
# To input a number and save it as an integer, you could do something like this:

# In[51]:


numberAsString = input("How old are you?")

number = int(numberAsString)
number = number + 5

print(f"In five years, you will be {number} years old")


# User input can quickly make a program take much longer to write and test. If you want to include it, you should wait until everything else works.

# ---
# 
# ### In-Class User Input Exercises
# 
# **a)** Write a program that asks you for your name, and prints it out with a greeting.
# 
# **b)** Write a program that takes a number as a user input, converts it to an integer, and prints out twice the number.
# 
# ---
