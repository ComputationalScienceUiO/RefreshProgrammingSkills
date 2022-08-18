#!/usr/bin/env python
# coding: utf-8

# # Linalg and numpy - Exercises

# In these exercises you will practice linear algebra in addition to the numpy library

# ### Task 1) Some basic numpy operations

# a) Check your numpy version and make sure the newest version is installed. You can use the following command:

# In[1]:


np.__version__


# The newest version per 18/8/21 should be version 1.21.0

# b) Create a matrix fillesd with 1's at each element. The matrix should be of shape 10x10, do not use numpy

# c) Now do the same thing as in b), but use numpy this time. **Bonus exercise:** Measure the time difference between the two implementations in ecercise b) and c)

# d1) First create an array of elements in an aranged order from 0 to 9, using np.arange.

# d2) Then use np.reshape to resahpe the array into the following matrix:
# 
# $$
# \begin{equation*}
# \begin{pmatrix}
# 1 & 4 & 7  \\
# 2 & 5 & 8  \\
# 3  & 6  & 9
# \end{pmatrix}
# \end{equation*}
# $$

# d3) Next task is to create some conditional statement, making all elements that are larger than 5 to be set as 1, and all elements that are less than 5 is set to 0, elements equal to 5 is unchanged.

# e) Create three random 1d arrays x, y and z of length 3. Use the numpy function vstack and hstack to stack the arrays both vertically and horizontally as a matrix.

# f) Create a random array of size 10. Print the mean, standard deviation and the variance using numpy

# ### Task 2) A bit of linear algebra

# a) Create a random matrix of size 3x3, containing only integers. Find the eigenvalues and eigenvectors using numpy.

# b) Is this matrix invertible? Compute the determinant

# c) If the matrix is invertible, find the invertible matrix

# d) Check if the following matrix is symmetric, real orthogonal, hermitian and unitary. Also find the norm of the matrix. 
#     
# $$
# \begin{equation*}
# \begin{pmatrix}
# 1-i & 1+i  \\
# 1+i & 1-i
# \end{pmatrix}
# \end{equation*}
# $$

# e) Find the LU decomposition of matrix A:
# 
# $$
# \begin{equation*}
# A=\begin{pmatrix}
# 1 & 2 & 4  \\
# 3 & 8 & 14  \\
# 2  & 6  & 13
# \end{pmatrix}
# \end{equation*}
# $$
# 
# What are the matrices L and U? You can try using numpy or scipy.linalg
#     

# In[ ]:




