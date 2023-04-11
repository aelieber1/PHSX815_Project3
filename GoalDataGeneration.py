"""
Goal Data Simulation Code for Project 3

Purpose: To randomly sample values from a poisson distribution given a certain ture rate parameter. 
The scenario that this is simulating is measurements of the number of goals per game across many
seasons. The rate parameter will be the only parameter deliberately changed when sampling data for the 
two hypotheses. Other parameters such as number of measurements and number of experiments can also be 
set by the user from the command line. For example, if the user sets Nmeas=10 and Nexp=5, then the code
will simulate data as if 10 games were observed, 5 times over, which means a total of 50 game score 
observations. 

Author: @aelieber1
Date: April 6, 2023
University of Kansas, PHSX 815 Computation Physics

Code Adapted from these sources: 
    - @crogan PHSX815 Github Week 1 & 2
    - Documentation for Numpy Poisson Random Sampling
    - Project 1 Data Generation Code
"""

# Import necessary external packages to use
from scipy.stats import poisson
import numpy as np
import sys

# import our Random class from Random.py file - contains Poisson method
sys.path.append(".") 
from Random import Random

# main function in Python to sample random data from a Poisson distribution for average number of goals per game

if __name__ == "__main__":
    
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-seed number]" % sys.argv[0])
        print (" -seed               seed value")
        print (" -rate               rate value, # goals per game")
        print (" -Nmeas              number of games observed per season")
        print (" -Nexp               number of seasons observed")
        print (" -output [filename]  filename to save data output to") 
        sys.exit(1)

    # default seed
    seed = 5555

    # default rate parameter (number of goals per game)
    rate = 1

    # default number of measurements which corresponds to games since we take one measurement a game
    Nmeas = 1

    # default number of experiments, number of times we observe set number of games e.g. seasons. 
    #(Ex. if Nmeas=10 and Nexp=5, then we will observe 10 games, 5 times over, observing 50 games total)
    Nexp = 1

    # output file defaults
    doOutputFile = False

    # read the user-provided seed from the command line (if there)
    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = sys.argv[p+1]
    if '-rate' in sys.argv:
        p = sys.argv.index('-rate')
        ptemp = float(sys.argv[p+1])
        if ptemp > 0:
            rate = ptemp
    if '-Nmeas' in sys.argv:
        p = sys.argv.index('-Nmeas')
        Nt = int(sys.argv[p+1])
        if Nt > 0:
            Nmeas = Nt
    if '-Nexp' in sys.argv:
        p = sys.argv.index('-Nexp')
        Ne = int(sys.argv[p+1])
        if Ne > 0:
            Nexp = Ne
    if '-output' in sys.argv:
        p = sys.argv.index('-output')
        OutputFileName = sys.argv[p+1]
        doOutputFile = True

    # class instance of our Random class using seed - It will call for the data to be sampled from a poisson distribution
    random = Random(seed)
    
    # sample data and either output in the command window (else) or output in a text file as named in the command line after -output
    if doOutputFile:
        outfile = open(OutputFileName, 'w')
        outfile.write(str(rate)+" \n")
        for e in range(0,Nexp):
            for t in range(0,Nmeas):
                outfile.write(str(random.Poisson(rate))+" ")
            outfile.write(" \n")
        outfile.close()
    else:
        print(rate)
        for e in range(0,Nexp):
            for t in range(0,Nmeas):
                print(random.Poisson(rate), end=' ')
            print(" ")
            
            