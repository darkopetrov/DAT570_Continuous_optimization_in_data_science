import numpy as np
from sklearn.linear_model import LogisticRegression


data=np.zeros((683,10))
label=np.zeros(683)
count=0


# The file for the dataset is found in the assignment
with open('breast-cancer.txt', 'r') as f:
    for x in f:
        x1=x.strip()
        y=x1.split(' ')
        label[count]=(float(y[0])-2)/2
        for k in range(10):
            h=y[k+2].split(':')
            # Here we make the distinction between the first variable and the rest
            # You should implement the two cases
            if k==0:
                data[count,k]=float(h[1])/1000000
            else:
                data[count,k]=float(h[1])
        count+=1

            
# here you have data and labels. Note that the labels are -1 and 1        

# Use the sklearn library to implent logistic regression
# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
# Train by the ".fit" method
# After training you can calculate the predictions by the ".score" method or
# use ".predict" method and count manually


print(t)
