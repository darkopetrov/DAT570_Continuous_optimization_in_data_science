import numpy as np

def EM_clustering(X,sigma,K):
    # Number of iterations
    iter_num=10
    # d is the number of features and n is the number of the data points:
    (n,d)=X.shape
    # Initialize the K centroids randomly. Each row is a centroid.
    M=np.random.randn(K,d)
    # A vector that stores the NLL value in different iterations:
    value=np.zeros(iter_num)

    #start the EM loop:
    for k in range(iter_num):
        # Apply the E stape by calculating the omega_{i,k} coefficients
        # Apply the M step and obtain an update of M
        # Calculate the NLL vale
        value[k]= ...

    return M, value


#Load the CC General dataset by pandas and keep the numerical part as a
# numpy array X

# Apply EM_clustering(X,sigma,K)
# Plot value vs iterations
# Apply different numbers of clusters and plot the last
# value of NLL (i.e. value[-1]) as the optimal NLL vs the number of clusters
