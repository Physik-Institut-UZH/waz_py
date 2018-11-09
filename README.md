# wazpo
Warp Zero Postprocessing

### Installation

First setup the enviroment:

```bash
cd wazpo 
conda env create -f environment.yml
conda activate wazpo  
```
This creates an environment with conda and installs, local to that environment, all the necessary packages. 
The third line activates the environment, you need call that line every time you want to use this library.
**NOTE:** the environment runs python=2.7.

Now install the executable:
```
pip install -e .
```
This will add to the enviroment an executable called: **wazpo**, that one can use to call directly from shell.



