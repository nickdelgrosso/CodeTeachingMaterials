import pickle
from scipy import optimize, stats
import matplotlib.pyplot as plt
import numpy as np
plt.ion()

#Load data from convertData.py
with open('velocity_data.pickle') as file:
	dat = pickle.load(file)



##### Absolute Acceleration ######
#Fit Gamma curve to the absolute acceleration data
def gammaFit(x,a,b): 
	curve = stats.gamma.pdf(x,a,scale=b)
	curve /= np.sum(curve)
	return curve

gammaParams, gammaCov = optimize.curve_fit(gammaFit, dat['acc'], dat['acc_pdf'])

#Plot
plt.figure(4)
plt.clf()

plt.subplot(1,2,1)
plt.scatter(dat['acc'],dat['acc_pdf'])

curve = stats.gamma.pdf(dat['acc'],gammaParams[0],scale=gammaParams[1])
plt.plot(dat['acc'], curve/np.sum(curve))



##### Direction Acceleration ######


#Fit Exponential curve to the direction acceleration data
def exponFit(x,a): 
	curve = stats.laplace.pdf(x,0,scale=a)
	curve /= np.sum(curve)
	return curve

exponParams, exponCov = optimize.curve_fit(exponFit, dat['dir'], dat['dir_pdf'])
laplaceParams = exponParams

#Plot the two curves
plt.subplot(1,2,2)
plt.scatter(dat['dir'],dat['dir_pdf'])

curve = stats.laplace.pdf(dat['dir'],0,scale=exponParams[0])
plt.plot(dat['dir'], curve/np.sum(curve))



#Print parameters and output to file
print 'Gamma Parameters: {0}'.format(gammaParams)
print 'Laplace Parameters: {0}'.format(laplaceParams)

with open('ratParams.pickle','wb') as file:
	pickle.dump(gammaParams,file)
	pickle.dump(laplaceParams,file)



plt.show()
