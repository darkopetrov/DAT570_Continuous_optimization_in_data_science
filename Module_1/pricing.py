import pandas
import numpy as np
from sklearn.linear_model import Ridge
# We will be using the sklearn library. You can learn more here:
# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html


# Loading the data
data0=pandas.read_csv('Real estate.csv')
npdata=data0.to_numpy()

# Divide the data to the variables and the label (price)
# The Ridge class does not admit an intercept (i.e. mu in the assignment) you should
# add a suitable column to your variables that will provide an extra parameter
# i.e. mu. Think what this column should be

# Now run ridge regression. Note that in the ridge classe mu is known as alpha.
#Setting alph=0 gives you the maximum likelihood solution. 
# You should try really large values of alpha to see the difference


