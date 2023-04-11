"""
Goal Data Analysis Code for Project 3

Purpose: 
    - You'll find several print statements throughout the code below, those are generally used to help
      troubleshoot while writing code, but they are left in the event you need to also troubleshoot 
      the results you get

Author: @aelieber1
Date: April 6, 2023
Code adapted from these sources: 

"""

# Import Necessary Packages
import sys
import math
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import poisson
from scipy.optimize import minimize


# main function for our CookieAnalysis Python code
if __name__ == "__main__":
   
    # Read in data file name from commandline prompt
    haveInput = False
    
    # To pass in the data file to be analyzed from the command line
    if '-input' in sys.argv:
        p = sys.argv.index('-input')
        InputFile = sys.argv[p+1]
        haveInput = True
    
    if '-h' in sys.argv or '--help' in sys.argv or not haveInput:
        print ("Usage: %s [options] [input file]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print (" -input (filename)   first hypothesis data to be analyzed")
        sys.exit(1)
        
    """ Negative log likelihood of Poisson function """ 
    # this function will be minimized later to ascertain what the probable value for 
    # the rate parameter lambda for each experiment 
    
    def loglikelihood(l):
        return (-1 * ((math.log(l) * sum_data) - (Nmeas * l) - factorial_sum))
        
    """ Estimate the Most Probable Lambda Value for the Dataset """
    need_rate = True
    with open(InputFile) as ifile: 
        
        # Read in true rate parameter
        for line in ifile:
            if need_rate:
                need_rate = False
                rate = float(line)
                continue
        print("True Rate is: ", rate)
        
        # Read in Nmeas (number of measurements)
        lineVals = line.split()
        Nmeas = len(lineVals)
        print("Nmeas: ", Nmeas)
        
        # Load data - skipping first row which just has the true rate
        data = np.loadtxt(InputFile, dtype=float, skiprows=1)
        #print(data)
                            
        # loop over each experiment
        Nexp = 0
        
        # Create empty arrays to store estimates of lambda, neg logliklihood, and error 
        param_estimates = []
        neg_logliklihood_estimates = []
        
        
        for i in data: 
            
            # Update counter for Nexp
            Nexp += 1
            
            """ Make calculations to use in minimization routine """
            # easier to troubleshoot this way rather than inputting it all into the 
            # function definition
            exp_data = i
            #print("Exp data: ", exp_data)
            sum_data = sum(exp_data)
            
            factorial_sum = 0
            for k in exp_data:
                f = math.log(math.factorial(k))
                factorial_sum += f
            
            # Add bounds - only values that should be considered to be the rate (lambda) 
            # should be positive zero to positive infinity
            rate_bounds = [(0, math.inf)]
            
            """ Find Minimum of Negative Log Liklihood Function """
            min_result = minimize(loglikelihood, x0=3, bounds=rate_bounds)
            print(" Minimization Routine Result: \n", min_result)
            minimum_estimate = min_result.x[0]
            param_estimates.append(minimum_estimate)
            
            # Add loglikelihood value to list - to plot later on
            neg_logliklihood_estimates.append(loglikelihood(minimum_estimate))
            
            
        print("Param Estimates: ", param_estimates)
        print("Neg LL Calculations: ", neg_logliklihood_estimates)

        Nmeas_total = Nmeas * Nexp   

# TODO: Plot the poisson distribution to visualize the data

# TODO: Plot likelihood function - identify estimated rate (likelihood vs. lambda)

# TODO: Plot or visualize the estimation of the parameter lambda

# TODO: Calculate what the estiamted lambda is & variation from average of the datapoints (analytical answer)
                            
                
    