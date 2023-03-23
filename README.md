# FAST.Farm
Functions to either read or plot FAST.Farm files.

## Content of this repository
### readfile_VTK.py
Takes a dataframe consisting of wind velocity and domain properties as input to output two scaled axes and wind velocities in a format where it can be visualized. The function uses x and y as variable names, but it works for any plane: XY, XZ, YZ. Just have to provide domain properties accordingly.

### Example1.py
An example of how the function readfile_VTK.py can be used.
In this example, the function is used to visualize a single .vtk file.
