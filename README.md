# FAST.Farm
Functions to either read or plot FAST.Farm files. Made for beginner FAST.Farm users, which I am myself. Code is made specifically for OpenFAST/FAST.Farm, but can probably be used elsewhere with slight tweaks. 

## Content of this repository
### readfile_VTK.py
Takes a dataframe consisting of wind velocity and domain properties as input to output two scaled axes and wind velocities in a format where it can be visualized. The function uses x and y as variable names, but it works for any plane: XY, XZ, YZ. Just have to provide domain properties accordingly.

### Example1.py
An example of how the function readfile_VTK.py can be used.
In this example, the function is used to visualize a single .vtk file.

### Example1.py
An example of how the function readfile_VTK.py can be used.
In this example, the .vtk files in a folder were averaged to create an average wake behind the turbine.
