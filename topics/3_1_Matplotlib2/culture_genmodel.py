import numpy as np

# Set random generator to the same state for everyone (random-but-predetermined data)
np.random.seed(42)

# Set the parameters for the analysis
n = 50

# Print starting message
print("Starting to Generate Model Simulation...")

# Generate variables for dataset
time = np.linspace(0, 12, num=n);
culture_a_model = (time + 3) ** 1.2
culture_b_model = (time + 1) ** 1.4

# Combine the variables into an array
data = np.array([time, culture_a_model, culture_b_model])
data = data.T

# Save the array to a file
np.savetxt('culture_growth_model.txt', data)

# Save the names of each column to another file
f = open('culture_growth_model_names.txt', 'w')
var_names = ['time', 'culture_a_model', 'culture_b_model']
var_names_string = "\n".join(var_names)
f.write(var_names_string)
f.close()

# Print ending message
print('...Done!')