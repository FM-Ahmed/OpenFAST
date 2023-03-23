#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np
import os

def readfile_VTK(data_vtk, xgrid, ygrid, x0, y0, xres, yres):
#     Inputs:
#         data_vtk: dataframe consisting of velocity data from .vtk file

#     Following input parameters (domain properties) can be found in the primary FAST.Farm input file (.fstf)
#         xgrid: number of low resolution spatial nodes in x-direction [scalar]
#         ygrid: number of low resolution spatial nodes in y-direction [scalar]
#         x0: starting x in low resolution domain [scalar]
#         y0: starting y in low resolution domain [scalar]
#         xres: resolution of low resolution domain in x-direction [scalar]
#         yres: resolution of low resolution domain in y-direction [scalar]

#     The function uses x and y as variable names, but the function works for all planes: XY, XZ, YZ
#     E.g YZ-plane: xgrid would be number of nodes in y-direction instead of x-direction
#     E.g. YZ-plane: ygrid would be number of nodes in z-direction instead of y-direction
#     Adjust inputs accordingly

#     Outputs:
#     x: scaled x-axis [(xgrid, ) array]
#     y: scaled y-axis [(ygrid, ) array]
#     u: wind velocities [(ygrid, xgrid) list]
    
    df_vtk = pd.DataFrame(data_vtk)
    x = np.arange(0, xgrid, 1)
    y = np.arange(0, ygrid, 1)
    np_vtk = df_vtk.to_numpy()
    templist = [] 

    i = 0
    while i < len(df_vtk):
        num = np_vtk[i][0]
        templist.append(num)
        i += 1
    u = [templist[i:i+xgrid] for i in range(0, len(templist), xgrid)]
    
    x = x*xres+x0
    y = y*yres+y0
    return x, y, u

