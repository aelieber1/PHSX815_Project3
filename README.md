# PHSX815_Project3

## Simple Simulation of Soccer Goals Using a Poisson Distribution & Subsequent Rate Parameter Estimation Analysis 

### This repository contains several programs:

- `GoalDataGeneration.py` [Python]
- `GoalDataAnalysis.py` [Python]
- `Random.py` [Python]

### You will see several TestData files, the instructions below list how to read them.

In order to read what these data files were generated off of, there are three numbers you need. The number of experiments, measurements per experiment, and the true lambda parameter. For the file, `TestData_100_100_4.txt` the numbers follow that same order. The dataset was generated for 100 experiments, 100 measurements for each experiment, and based off of a true rate parameter of 4. Each of the following files found in this repository can be read in a similar manner. 

- `TestData_100_100_4.txt`
- `TestData_1000_100_4.txt`
- `TestData_10_100_3.txt`
- `TestData_10_1000_3.txt`
- `TestData_10_10000_3.txt`

Of course, using the `GoalDataGeneration.py` [Python], you can generate any data set you'd like based off of the parameters you'd like! The world is your oyster!

### Requirements

The Python code in this repository requires the use of several packages which can be 
easily installed from the command line using `HomeBrew` or `pip install` commands. 

In order to compile the program `GoalDataGeneration.py`, these external 
packages are required:
- `numpy`
- `from scipy.stats import poisson`

In order to compile the programs `GoalDataAnalysis.py`, these external 
packages are required:
- `math`
- `numpy`
- `matplotlib.pyplot as plt`
- `scipy.stats` import `poisson`
- `from scipy.optimize import minimize`
- `from scipy.special import gammaln`

### Usage

The python file `GoalDataGeneration.py` which simulates the experiment can be run from the command
line by typing:

	<> python3 GoalDataGeneration.py -rate [rate] -seed [seed] -Nmeas [number of games observed] -Nexp [number of sets of measurments or seasons observed] -output ["filename"]

This script will either print the result to the command line or save to a file if given a filename from the command line. See earlier section to understand the datasets present in the repository already. 

With the two datasets on hand from the previous script, the next python file to run is `GoalDataAnalysis.py`  which can be run from the commandline by typing:

	<> python3 GoalDataAnalysis.py -input ["filename"]

This script will conduct our analysis of estimating the rate parameter that is most probable based on the dataset using various methods. 

### Other Notes

- All of the Python programs can be called from the command line with the `-h` or `--help` flag, which will print the options

- The files and `Random.py` are called within the scripts and should be downloaded or cloned to run properly


    
    
