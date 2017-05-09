import numpy as np
import matplotlib.pyplot as plt

def savitzky_golay(y, weight_vector, window_size, order, deriv=0):
    """
    INPUT: NDARRAY, NDARRAY, INT, INT, INT
    OUPUT: NDARRAY
    Savitzky_Golay filter with weighted data point
    REFERENCE: https://en.wikipedia.org/wiki/Savitzky%E2%80%93Golay_filter
    """

    try:
        window_size = np.abs(np.int(window_size))
        order = np.abs(np.int(order))
    except ValueError, msg:
        raise ValueError("window_size and order have to be of type int")
    if window_size % 2 != 1 or window_size < 1:
        raise TypeError("window_size size must be a positive odd number")
    if window_size < order + 2:
        raise TypeError("window_size is too small for the polynomials order")
    order_range = range(order+1)
    half_window = (window_size -1) // 2
    
    y = np.hstack((y[1 : half_window + 1][::-1], y, y[len(y)-half_window : len(y)][::-1]))
    weight_vector = np.hstack((weight_vector[1 : half_window + 1][::-1], 
	    			weight_vector, 
				weight_vector[len(weight_vector)-half_window : len(weight_vector)][::-1]))
    
    y_hat = []

    b = np.mat([[k**i for i in order_range] for k in range(-half_window, half_window+1)]) 

    for i in range( half_window, len(y)-half_window):
	w = weight_vector[ i - half_window : i + half_window + 1]
	y_i = y[i - half_window : i + half_window + 1] * w 

	w_i = np.repeat(w, order + 1).reshape(-1, order + 1)
	b_i = np.multiply(b, w_i)
	coef = np.linalg.pinv(b_i).A[deriv]
    	y_hat.append(np.dot(y_i, coef))
	
    return y_hat 

if __name__ == "__main__":
	#mod_ref =  np.loadtxt("../data/FuentesAndalucia_MOD09A1.txt", delimiter=";")
	#ndvi = (mod_ref[:,8] - mod_ref[:,7])/(mod_ref[:,8]+mod_ref[:,7])
	#plt.plot ( ndvi, 'k-', label="MOD09 NDVI")
	import pandas as pd
	from scipy.signal import savgol_filter
	
	data = pd.read_csv('ndvi_raw.csv')
	x = [0.5, 1, 0]
	w = np.random.choice(x, 10)
		
	ndvi = data.iloc[5000, :]
	print 'ndvi', ndvi.values
	savitzky_golay(ndvi, np.ones(46), window_size=7, order=2)

	yhat = savgol_filter(ndvi, 7, 2, mode='mirror')
	#print [ndvi]
	#print 'so,', ndvi_smooth
	print 'yhat--scipy', yhat
	#print len(ndvi_smooth)
	
	#plt.plot ( ndvi_smooth, '-r', label="Smooth NDVI", lw=1.5)
	#plt.legend(loc='best' )
	#plt.grid ( True ) 
	#plt.show()
	#plt.savefig('images/golay.png')

