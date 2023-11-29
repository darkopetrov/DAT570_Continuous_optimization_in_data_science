import imageio.v2 as iio
import matplotlib.pyplot as plt
import numpy as np
import scipy.fftpack as transform

img = iio.imread("panda.png")
# generating grayscale image:
bw_img=np.sum(img,2)/3

# 2D DCT transform 
coeffs= transform.dct(transform.dct(bw_img, axis=0),axis=1)

# Set a threshold t and threshold the coefficients in coeffs which will generate
# approx_coeffs also calculate the fraction of nonzero coefficients


# Apply 2d idct
approx_img=transform.idct(transform.idct(approx_coeffs, axis=1),axis=0)

#
plt.imshow(approx_img, cmap='gray')
plt.show()
