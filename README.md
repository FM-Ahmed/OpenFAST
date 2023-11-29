Functions to either read or plot FAST.Farm/OpenFAST/TurbSim files. These are wind simulation tools developed by NREL. The scripts are made for beginner users, which I am myself. Code is made specifically for OpenFAST/FAST.Farm, but can probably be used elsewhere with slight tweaks. May or may not work for other versions of the software.

# FAST.Farm v3.4.1

### readfile_VTK.py
Takes a dataframe consisting of wind velocity and domain properties as input to output two scaled axes and wind velocities in a format where it can be visualized. The function uses x and y as variable names, but it works for any plane: XY, XZ, YZ. Just have to provide domain properties accordingly.

### Example1.py
An example of how the function readfile_VTK.py can be used.
In this example, the function is used to visualize a single .vtk file.

### Example1.py
An example of how the function readfile_VTK.py can be used.
In this example, the .vtk files in a folder were averaged to create an average wake behind the turbine.

# OpenFAST v3.4.1

### plot_outfile.py

Takes absolute path to .out file from OpenFAST and a list of requested variables as inputs to plot them in subplots with correct units. Depending on the size of the .out file, it might take a bit of time. Not a function, run whole script with above-mentioned inputs to get the plots. Number of requested variables must be longer than 2.

# TurbSim v2.00

### read_dotprofiles.py

Function that returns wind speed array (u) and corresponding height array (z) from .Profiles input file for TurbSim v2.00 (for OpenFAST v3.4.1).

### makefile_Profiles.py

To use a user-defined wind profile as input in TurbSim this filetype and structure is needed. This function creates this file (with extension .Profiles) at a specific folder with a specific name. For TurbSim v2.00, may or may not work for other versions (last updated April 2023). For use for simple wind profiles with no veer and direct wind inflow at turbine (0 deg wind direction). 
