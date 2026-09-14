# *****Project 1: CadQuery*****
# Name: 
# Don't change the next 4 lines! 
import os
import cadquery as cq
from ocp_vscode import show, set_port
set_port(3939)

# Example base object code. Run it once to check if everything works! 
height = 60.0
width = 80.0
thickness = 10.0

# make the base
result = cq.Workplane("XY").box(height, width, thickness)





# Renders the solid
show(result)

# Uncomment (remove #) the last 5 lines to have your design exported as a STL file in your project folder
#current_folder = os.path.dirname(os.path.abspath(__file__))
#export_path = os.path.join(current_folder, 'my_cad_block.stl')
#print("[*] Exporting model to STL for 3D printing...")
#cq.exporters.export(result, 'my_cad_block.stl')
#print("Export complete!")
