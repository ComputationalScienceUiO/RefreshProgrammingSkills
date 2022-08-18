#!/usr/bin/env python
# coding: utf-8

# # scikit-learn - Exercises

# In this exercise you are going to perform regression on a dataset you create yourself

# ### Task 1) Load/Create the dataset

# The first thing to do when dealing with machine learning is to have the dataset ready. Make a dataset containing 100 datapoints generated using an uniform distribution. The target variable y is given by the following formula:
# 
# $$
# \begin{equation*}
#     y = 2.0+5x+0.1*N(0,1)
# \end{equation*}
# $$

# ### Task 2) Create a linear regression object and predict

# Create a linear regression object using scikit, and use it to perform a prediction on the dataset created in the task above.

# ### Task 3) Find the following statistical values

# Find the following statistical values for your prediction: intercept alpha, coefficient beta, mean squared error, the variance score, mean squared log error and the mean absolute error.

# ### Task 4) Plot the results

# Plot the predicted values in the same plot as the targeted values as a function of x.

# ### Task 5) Switching up the target function

# Do the same thing again, but switch up the target function with the following:
# 
# $$
# \begin{equation*}
#     y = x+2.0x^3+0.1*N(0,1)
# \end{equation*}
# $$
# 
# Now how does the prediction go?

# ### Task 6) Polynomial regression

# Now try predicting again using polynomial regression. How does the degree of polynomial you choose affect the predictions? What is the optimal degree of polynomial? Why, why not?

# ### Task 7) Extra task, if you have time

# Experiment with more types of machine learning models which can be found in the scikit learn library. For instance, ridge regression, lasso regression and logistic regression.

# In[ ]:




