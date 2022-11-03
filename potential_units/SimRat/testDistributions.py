from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

plt.ion()

x = np.arange(0,5,.02)

plt.figure(5)
plt.clf()
plt.title('Expon')

for a in np.arange(0,6,1):
	dist = stats.expon.pdf(x,0, scale=a)
	plt.plot(x,dist/np.sum(dist))

plt.show()
