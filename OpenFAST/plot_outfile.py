#!/usr/bin/env python
# coding: utf-8

# In[35]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# Inputs
path_to_file = r'' # put absolute path to .out file from OpenFAST inside brackets

user_inputs = ['TwrBsFxt', # put variables you want to plot in list
               'TwrBsFyt',
               'TwrBsMxt',
               'TwrBsMyt']

# From hereon, code does work, no more inputs needed under this line
if len(user_inputs) <= 2:
    raise ValueError('Length of user_inputs must be longer than 2. Length is currently {}.'.format(len(user_inputs)))
else:
    None

input_data = open(path_to_file)
data = pd.read_csv(input_data, header = 3, sep='\s+', lineterminator = '\n', dtype = str)
dfunit = pd.DataFrame(data)
df_data = dfunit[1:].loc[:,:].astype(float)

input_data.close()

# time variable
time = df_data['Time']

# check if the requested variables are valid or not
def check_variables():
    for input_variable in user_inputs:
        if input_variable in dfunit.columns:
            None
        else:
            raise KeyError('The requested variable {} is not valid'.format(input_variable))
    return print('All requested variables are ok.') 
check_variables()

# finding units for the variables
variable_unit_pairs = {}
for item in user_inputs:
    variable_unit_pairs[item] = dfunit[item][0]

# sorting variables and units into lists and dataframe, used in plotting
list_of_col = []
list_of_unit = []
for key, value in variable_unit_pairs.items():
    list_of_col.append(key)
    list_of_unit.append(value)

df = df_data[list_of_col].copy()

# checking how many input variables and making appropriate amount of subplots
evenNumbers = np.arange(2, 8002, 2)
oddNumbers = np.arange(1, 8001, 2)

if len(list_of_col) in evenNumbers:
    nrows = int(len(list_of_col)/2)
if len(list_of_col) in oddNumbers:
    nrows = int(len(list_of_col)/2) + 1

# making list of colors used in plotting
TABLEAU_COLORS_swapped = dict((v, k) for k, v in mcolors.TABLEAU_COLORS.items())
colordict = dict(TABLEAU_COLORS_swapped, **mcolors.BASE_COLORS)

list_of_colors = []
for key, value in colordict.items():
    list_of_colors.append(key)
list_of_colors.remove('w') # remove white color, cant see white plots
list_of_colors *= nrows

# plotting
fig, ax = plt.subplots(nrows, 2, figsize = [20, nrows*3], sharex = True)

i = 0
while (i < len(list_of_col)):
    if i < nrows:
        ax[i, 0].plot(time, df[df.columns[i]], color = list_of_colors[i])
        ax[i, 0].set_title(df.columns[i])
        ax[i, 0].grid(True, 'both')
        ax[i, 0].set_ylabel(list_of_unit[i])
    else:
        ax[i-nrows, 1].plot(time, df[df.columns[i]], color = list_of_colors[i-nrows])
        ax[i-nrows, 1].set_title(df.columns[i])
        ax[i-nrows, 1].grid(True, 'both')
        ax[i-nrows, 1].set_ylabel(list_of_unit[i])

    if i == nrows-1:
        ax[i, 0].set_xlabel('Time (s)')
        ax[i, 1].set_xlabel('Time (s)')
    i += 1
