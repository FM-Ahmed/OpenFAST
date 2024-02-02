#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import os

filepath = '' # absolute path to .vtk file you want to visualize

vtk_file = open(filepath)
data_vtk = pd.read_csv(vtk_file, header = 8, sep='\s+', lineterminator = '\n')
vtk_file.close()

# header should be set to 8 when providing an absolute path to the .vtk file
# otherwise, you might need to change it 

# input parameters gathered from primary FAST.farm input file (.fstf)
xgrid = 601
ygrid = 45
x0 = -2400
y0 = -264
xres = 12
yres = 12

x, y, u = readfile_VTK(data_vtk, xgrid, ygrid, x0, y0, xres, yres)

# visualize wind field
plt.figure(figsize = (18, 4)) # arbitrary figure size
plt.pcolormesh(x, y, u, cmap = cm.coolwarm, shading = 'auto')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.colorbar(orientation = 'horizontal', label = 'Wind speed (m/s)');

