# *****Project 1: CadQuery*****
# Name: 
# Don't change the next 2 lines! 
import cadquery as cq
from ocp_vscode import show

# Example base object code. Run it once to check if everything works! 
height = 60.0
width = 80.0
thickness = 10.0

# make the base
result = cq.Workplane("XY").box(height, width, thickness)

# Render the solid
show(result)
