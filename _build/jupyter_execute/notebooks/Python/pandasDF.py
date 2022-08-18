#!/usr/bin/env python
# coding: utf-8

# # pandas - DataFrame Intro
# 
# A very useful Python package is
# [pandas](https://pandas.pydata.org/), which is an open source library
# providing high-performance, easy-to-use data structures and data
# analysis tools for Python. **pandas** stands for panel data, a term borrowed from econometrics and is an efficient library for data analysis with an emphasis on tabular data.
# **pandas** has two major classes, the **DataFrame** class with two-dimensional data objects and tabular data organized in columns and the class **Series** with a focus on one-dimensional data objects. Both classes allow you to index data easily as we will see in the examples below. 
# **pandas** allows you also to perform mathematical operations on the data, spanning from simple reshapings of vectors and matrices to statistical operations. 
# 
# The following simple example shows how we can, in an easy way make tables of our data. Here we define a data set which includes names, place of birth and date of birth, and displays the data in an easy to read way. We will see repeated use of **pandas**, in particular in connection with classification of data.

# In[1]:


import pandas as pd
from IPython.display import display
data = {'First Name': ["Frodo", "Bilbo", "Aragorn II", "Samwise"],
        'Last Name': ["Baggins", "Baggins","Elessar","Gamgee"],
        'Place of birth': ["Shire", "Shire", "Eriador", "Shire"],
        'Date of Birth T.A.': [2968, 2890, 2931, 2980]
        }
data_pandas = pd.DataFrame(data)
display(data_pandas)


# In the above we have imported **pandas** with the shorthand **pd**, the latter has become the standard way we import **pandas**. We make then a list of various variables
# and reorganize the aboves lists into a **DataFrame** and then print out  a neat table with specific column labels as *Name*, *place of birth* and *date of birth*.
# Displaying these results, we see that the indices are given by the default numbers from zero to three.
# **pandas** is extremely flexible and we can easily change the above indices by defining a new type of indexing as

# In[2]:


data_pandas = pd.DataFrame(data,index=['Frodo','Bilbo','Aragorn','Sam'])
display(data_pandas)


# Thereafter we display the content of the row which begins with the index **Aragorn**

# In[3]:


display(data_pandas.loc['Aragorn'])


# We can easily append data to this, for example

# In[4]:


new_hobbit = {'First Name': ["Peregrin"],
              'Last Name': ["Took"],
              'Place of birth': ["Shire"],
              'Date of Birth T.A.': [2990]
              }
data_pandas=data_pandas.append(pd.DataFrame(new_hobbit, index=['Pippin']))
display(data_pandas)


# Here are other examples where we use the **DataFrame** functionality to handle arrays, now with more interesting features for us, namely numbers. We set up a matrix 
# of dimensionality $10\times 5$ and compute the mean value and standard deviation of each column. Similarly, we can perform mathematial operations like squaring the matrix elements and many other operations.

# In[5]:


import numpy as np
import pandas as pd
from IPython.display import display
np.random.seed(100)
# setting up a 10 x 5 matrix
rows = 10
cols = 5
a = np.random.randn(rows,cols)
df = pd.DataFrame(a)
display(df)
print(df.mean())
print(df.std())
display(df**2)


# Thereafter we can select specific columns only and plot final results

# In[6]:


df.columns = ['First', 'Second', 'Third', 'Fourth', 'Fifth']
df.index = np.arange(10)

display(df)
print(df['Second'].mean() )
print(df.info())
print(df.describe())

from pylab import plt, mpl
plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'

df.cumsum().plot(lw=2.0, figsize=(10,6))
plt.show()


df.plot.bar(figsize=(10,6), rot=15)
plt.show()


# We can produce a $4\times 4$ matrix

# In[7]:


b = np.arange(16).reshape((4,4))
print(b)
df1 = pd.DataFrame(b)
print(df1)


# and many other operations. 
# 
# The **Series** class is another important class included in
# **pandas**. You can view it as a specialization of **DataFrame** but where
# we have just a single column of data. It shares many of the same features as _DataFrame. As with **DataFrame**,
# most operations are vectorized, achieving thereby a high performance when dealing with computations of arrays, in particular labeled arrays.
# As we will see below it leads also to a very concice code close to the mathematical operations we may be interested in.
# For multidimensional arrays, we recommend strongly [xarray](http://xarray.pydata.org/en/stable/). **xarray** has much of the same flexibility as **pandas**, but allows for the extension to higher dimensions than two. We will see examples later of the usage of both **pandas** and **xarray**. 
# 
# 
# 
# 
# 
# 
# In order to study various Machine Learning algorithms, we need to
# access data. Acccessing data is an essential step in all machine
# learning algorithms. In particular, setting up the so-called **design
# matrix** (to be defined below) is often the first element we need in
# order to perform our calculations. To set up the design matrix means
# reading (and later, when the calculations are done, writing) data
# in various formats, The formats span from reading files from disk,
# loading data from databases and interacting with online sources
# like web application programming interfaces (APIs).
# 
# In handling various input formats, as discussed above, we will mainly stay with **pandas**,
# a Python package which allows us, in a seamless and painless way, to
# deal with a multitude of formats, from standard **csv** (comma separated
# values) files, via **excel**, **html** to **hdf5** formats.  With **pandas**
# and the **DataFrame**  and **Series** functionalities we are able to convert text data
# into the calculational formats we need for a specific algorithm. And our code is going to be 
# pretty close the basic mathematical expressions.

# In[ ]:




