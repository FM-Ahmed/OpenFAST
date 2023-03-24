#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import os

# averages .vtk files in a folder and returns averaged wind field
path_to_folder = '' # specify path to the folder where the .vtk files are stored
allfiles = os.listdir(path_to_folder)

vtkfiles = []
for item in allfiles:
    if 'XY' in item: # specify plane (XY, XZ, YZ)
        vtkfiles.append(item)

list_of_wakes = []
for i in range(len(vtkfiles)):
    vtk_file = str(path_to_folder) + str('\\') + str(vtkfiles[i])
    data_vtk = pd.read_csv(vtk_file, header = 8, sep='\s+', lineterminator = '\n')
    list_of_wakes.append(data_vtk)

startup = 300 # remove startup time (in seconds) to remove startup effects (set = 0 if this is not wanted)
list_of_wakes = list_of_wakes[startup:]
averaged_wake = sum(list_of_wakes)/len(list_of_wakes)

# input parameters gathered from primary FAST.farm input file (.fstf)
xgrid = 601
ygrid = 45
x0 = -2400
y0 = -264
xres = 12
yres = 12

x, y, u_avg = readfile_VTK(averaged_wake, xgrid, ygrid, x0, y0, xres, yres)

# visualize wind field
plt.figure(figsize = (18, 4)) # arbitrary figure size
plt.pcolormesh(x, y, u_avg, cmap = cm.coolwarm, shading = 'auto')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.colorbar(orientation = 'horizontal', label = 'Wind speed (m/s)');

