# PHSX815_Project3 UPDATE ME PLEASE!!!!

## Simple Simulation of Soccer Goals Using a Poisson Distribution & Hypothesis Testing

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

The python file `GoalData.py` which simulates the experiment can be run from the command
line by typing:

	<> python3 GoalData.py -rate [rate] -seed [seed] -Nmeas [number of games observed] -Nexp [number of sets of measurments or seasons observed] -output ["filename"]

This script will either print the result to the command line or save to a file if given a filename from the command line.

The other files in the repository `H0_data_lam_3_10000.txt`, `H1_data_lam_5_10000.txt`, `H1_data_lam_9_10000.txt` are examples of data textfiles that were the output of running `GoalData.py` under different rate parameters for 20 measurements per 10000 experiments. 


With the two datasets on hand from the previous script, the next python file to run is `GoalDataAnalysis.py`  which can be run from the commandline by typing:

	<> python3 GoalData.py -inputH0 ["filename"] -inputH1 ["filename"]

This script will conduct our analysis and hypothesis testing of these two datasets and output two plots, (1) a histogram of the data provided from both hypotheses, and (2) a log likelihood ratio plot which includes the critical lambda value and the final power of the test calculated. 

### Other Notes

- All of the Python programs can be called from the command line with the `-h` 
or `--help` flag, which will print the options

- The files `MySort.py` and `Random.py` are called within the scripts adn should be 
downloaded or cloned to run properly


    
    
