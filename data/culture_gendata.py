import numpy as np

# Set random generator to the same state for everyone (random-but-predetermined data)
np.random.seed(42)

# Set the parameters for the analysis
n = 40

# Print starting message
print("Starting to Generate Data...")

# Generate variables for dataset
time = np.linspace(0, 11, num=n)
culture_a_data = (time + 3) ** 1.2 + np.random.normal(0, 2, size=n)
culture_b_data = (time + 1) ** 1.35 + np.random.normal(0, 3, size=n)

# Combine the variables into an array
data = np.array([time, culture_a_data, culture_b_data])
data = data.T

# Save the array to a file
np.savetxt('culture_growth_data.txt', data)

# Save the names of each column to another file
f = open('culture_growth_data_names.txt', 'w')
var_names = ['time', 'culture_a_data', 'culture_b_data']
var_names_string = "\n".join(var_names)
f.write(var_names_string)
f.close()

# Print ending message
print('...Done!')