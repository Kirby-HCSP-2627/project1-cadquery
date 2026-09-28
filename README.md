# project1-setup

### INSTALL (Run this first)
#### Install Mamba
[For Windows, Click Here](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe)
1. Next, open Miniforge Prompt from Windows Start Menu
2. Type:
```bash
conda init
```

[For M series Mac, Click Here](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-arm64.pkg) (If you are unsure, ask me) <br/>
No extra steps for you! 

#### Setup your vscode
Before you start, clone the directory into your folder.<br/>
Make sure you open your terminal while in your projects folder. 
Run the commands, one at a time: 
```bash
mamba env create -f environment.yaml
```
```bash
mamba activate project1-cadquery
```
If you receive a **"Shell not initialized"** error when running the activate command, run this to grant Mamba permission to manage your terminal:
```bash
mamba shell init --shell zsh --root-prefix=~/miniforge3
```
If you are running Windows use this command instead
```bash
mamba shell init --shell powershell --root-prefix=$env:USERPROFILE\miniforge3
```
After running the initialization command, **fully close your terminal window**, open a fresh one, navigate back into your folder, and run
```bash
mamba activate project1-cadquery
```
You will know it works if you see (project1-cadquery) in the left side of your command line. <br/>
We are almost there! You will get some pop-ups to install extensions. Install all of them. <br/>
Finally, on the left vertical side bar find the ocp extension. Click the select python interpreter. Choose the project1-cadquery option.

### Relevant Info
Use the documentation found [here.](https://cadquery.readthedocs.io/en/latest/) I found the QuickStart and Examples sections the most useful!

```python
# Create the base box using our dimensions
body = cq.Workplane("XY").box(100, 75, 50, centered=(True, True, False)) # Last value is false because we aren't working on z-axis

pocket1 = (
    cq.Workplane("XY")
    .workplane(offset=10) # Why would I need an offset? 
    .box(60 , 40, 20, centered=(True, True, False))  # Creates box at center
    .translate((-50, 30, 0)) # Move the center to the left 50mm and up 30mm
)

# Cut from the body
organizer = body.cut(pocket1) # If you have multiple you can call .cut() more than once Ex. body.cut(pocket1).cut(pocket2).cut(pocket3)
```

### The Program
Your task is to design a fully functional, 3D-printable parametric desk organizer using Python and the CadQuery script-based CAD modeling library. Instead of using drag-and-drop modeling software, you will write code to generate the 3D geometry mathematically. Your final code must be parametric, meaning that changing a few top-level variables (like wall thickness or compartment depths) will automatically resize the entire organizer without breaking the model. <br/><br/>

Your python script must output a single, modular 3D object that complies with the following constraints:<br/>
1. The base dimensions of the desk organizer can be no larger than 8 inches by 8 inches.
2. Must feature a compartment capable of holding at least 10 pencils or pens.
3. Dedicated slots to securely hold at least 5 markers, think sharpies or highlighters.
4. A container/tray area designed to hold loose, small items like paper clips and binder clips.
5. A dedicated slot to hold a standard passport-sized notebook.
6. Must feature a slanted tray or a tilted slot designed to prop up a smartphone at a readable angle.

### Example Output
<img width="1258" height="781" alt="Screenshot 2026-09-28 at 9 52 30 AM" src="https://github.com/user-attachments/assets/3aeb802f-19f9-4b1f-99c5-aa77d712bc3e" />
Your code should render an image on the OCP CAD Viewer tab on VSCode.

### Testing
No testing for this project. Most projects won't run tests since they are more open ended. I will be manually reviewing your code. 

### Submitting 
To submit your project:<br/>
1. Open a terminal window in vscode in your project folder
2. Replace file_name with the name of the file you edited
```bash
git add file_name.py
```
3. Type short summary of what you added in between quotations
```bash
git commit -m "your message here"
```
4. Push it to your repository
```bash
git push
```
5. Confirm on your GitHub account, might take ~1 or 2 minutes to update on GitHub website
