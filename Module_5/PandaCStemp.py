import imageio.v2 as iio
import matplotlib.pyplot as plt
import numpy as np
import scipy.fftpack as transform


# Take a number sample_num of samples and generate their
# horizontal and vertical coordinates (indicies) randomly in arrays xcoord, ycoord
# Store these samples in an array called y.

# The goal is to find the dct components x of the image from y and
# then use inverse dct to reconstruct the image.

def sq_loss_gradient(x,y, xcoord, ycoord):
    # samp_approx is Ax
    img_approx= transform.idct(transform.idct(x, axis=1, norm='ortho'),axis=0, norm='ortho')
    samp_approx=np.zeros((samp))
    for l in range(sample_num):
        samp_approx[l]=img_approx[xcoord[l],ycoord[l]]

    # The following calculates e=Ax-y
    error=samp_approx-samples
    img_err=np.zeros(bw_img.shape)
    for l in range(samp):
        img_err[xcoord[l],ycoord[l]]=error[l]
    # This calculates A^Te which is the gradient 
    grad=transform.dct(transform.dct(img_err, axis=0, norm='ortho'),axis=1, norm='ortho')

    return grad

def shrinkage(x,alpha):
    # Implement the shrinkage operator which is the proximal operator
    # of the regularizer

def ISTA(samples, xcoord, ycoord, alpha, xinit, step=0.99, iternum=100):
    # Implement the ISTA algorithm as in the previous exercise
    # In this case, it should work for any step size less than or equal 1
    # Your require the gradient function and the proximal function (shrinkage)
    # Initialization:
    x=xinit
    for iter in range(iternum):
        # Implement the iteration and also calculate the objective value and
        # the vaue of the regularization term at each iteration
    return x

def ISTA(samples, xcoord, ycoord, alpha, xinit, step=0.99, iternum=100):
    # Implement the FISTA algorithm similar to ISTA
    # It needs extra variables t and y


# run ISTA/FISTA and generate the approximate DCT coefficients x
# Then, generate the recovered image
img_approx= transform.idct(transform.idct(x, axis=1),axis=0, , norm='ortho')

# Plot the result
fig = plt.figure()    
plt.imshow(img_approx, cmap='gray')
fig.show()

