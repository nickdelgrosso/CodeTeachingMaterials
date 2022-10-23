import numpy as np

data = np.random.random(10)
np.savetxt(snakemake.output[0], data)