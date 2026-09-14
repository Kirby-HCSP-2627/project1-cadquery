# project1-setup

### INSTALL (Run this first)
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
This section will be a short description of the project and what it will be testing. <br/>

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
This section will have actual instructions for your project. Usually, in the format of expected inputs and expected results. 
This section will usually be the longest and with the most info! <br/>
1. For this project make a file called hello.py
2. In the file, write a print statement that outputs "Hello, world!"

### Example Output
Here I will include some example inputs and expected outputs. Think of it as an example and a quick check for your program. <br/>

### Testing
Finally, here I will provide a couple test cases that your code will be grade against. Along with their solutions. These will not be all of the test cases. Just some for you to check against. <br/>

### Submitting 
To submit your project:<br/>
1. Open a terminal window in vscode in your project folder
2. run git add file_name.py , replacing it for whatever file you wrote code to
3. run git commit -m "Type your message in between the quotation marks, your message should only be a couple words long and about what you changed"
4. run git push 
5. Confirm and check your auto-grade (if it's enabled) on your GitHub account, might take ~1 or 2 minutes to update on GitHub website
