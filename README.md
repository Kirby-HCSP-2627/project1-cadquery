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
mamba shell init --shell zsh --root-prefix=/opt/homebrew/Caskroom/miniforge/base
```
If you are running Windows use this command instead
```bash
mamba shell init --shell powershell --root-prefix=/opt/homebrew/Caskroom/miniforge/base
```
After running the initialization command, **fully close your terminal window**, open a fresh one, navigate back into your folder, and run
```bash
mamba activate project1-cadquery
```
You will know it works if you see (project1-cadquery) in the left side of your command line. <br/>
We are almost there! You will get some pop-ups to install extensions. Install all of them. <br/>
Finally, on the left vertical side bar find the ocp extension. Click the select python interpreter. Choose the project1-cadquery option.

### Intro
Coming soon! 

### Relevant Info
Use the documentation found [here.](https://cadquery.readthedocs.io/en/latest/) I found the QuickStart and Examples sections the most useful!

```python
# In general you will want to set your dimensions in a section like this
height = 60.0
width = 80.0
thickness = 10.0
diameter = 22.0

#Then use the result and combination of commands to make the base 
result = (
    cq.Workplane("XY")
    .box(height, width, thickness)
    .faces(">Z") # Selects top-most face
    .workplane() # Starts a new workplace on the selected face
    .hole(diameter) # Makes a hole on the new workplace
)
```

### The Program

1. For this project edit the file called main.py. This is where all of your code will go!

### Example Output
Coming Soon 

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
