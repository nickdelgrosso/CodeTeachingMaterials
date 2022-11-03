import numpy as np
from matplotlib import pyplot, mlab
from random import normalvariate
pyplot.ion()

#Set inputs
freq = 8.

start_time = 0
end_time = 1
time_resolution = .001

noise_sigma = .067	
noise_update_dt = .001 #in seconds


#Calculate phase of the oscillator
time = np.arange(start_time, end_time, time_resolution)

phase = [0]
last_update = 0
for t in time[1:]:
	
	#Calculate new phase for next time step from the last one.
	phase.append( phase[-1] + (time_resolution * 2.* np.pi * freq))

	#Every once in a while, add noise.
	if last_update == 0 or t > (last_update + noise_update_dt):
		last_update = t
		phase[-1] += normalvariate(0,noise_sigma)
	



#### Plots ####
pyplot.plot(time,np.sin(phase))
pyplot.show()



