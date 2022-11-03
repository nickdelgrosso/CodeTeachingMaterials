import numpy as np
import Image

""" Creates a .png image of a circle with darkness increasing to black toward the center.
"""


#Create array of distances, x and y, then a grid of combined distance from (0,0)
x = np.linspace(0,2000,2000)
x_grid, y_grid = np.meshgrid(x,x)

dist_grid = np.sqrt(x_grid**2 + y_grid**2)


#square the distances. 
dist_grid = dist_grid**2

#Scale by 255 (maximum whiteness value in 8-bit images)
dist_grid = 255 * dist_grid / np.max(dist_grid[0,:])
dist_grid_near = dist_grid <= 255.
dist_grid_far = dist_grid > 255.

dist_grid = (dist_grid * dist_grid_near) + (255. * dist_grid_far)



#Convert to image (RGB)
dist_grid = np.round(dist_grid)
dist_grid = dist_grid.astype(np.uint8)
dist_grid_3D = np.dstack((dist_grid, dist_grid, dist_grid))
img = Image.fromarray(dist_grid_3D, 'RGB')

#Save the Image
img.save('squareCirc.png')


