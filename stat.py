#!/usr/bin/env python3
# This program demonstrates a way to get arguments and options from command line
import sys
import pandas as pd

# You should use more appropriately named variable names than me.
# I just don't know what your options are.
# In my example two options are just present or not, but the third requires a number to follow.
# By initalising the option to None, you can later tell that you did not get this option.
# If you initialise it to a value instead, then that becomes a default value, ready to use. 
optionA, optionM, optionNumber, optionN, optionB = None, None, None, None, None
filename = None

# By creating a usage function, you can always call that. Makes it easy to be user friendly
def usage(msg=None):
    # Print a message if there was something specific you want to the user. 
    if msg is not None:
        print(msg, "\n")
    print ("Usage: demooption.py [-a] [-b] [-c <integer>] <filename>")
    # Exit the program. We can not progress. Makes logic easier elsewhere.
    sys.exit(1)

# Command line parsing
# This can be done in different ways. This is just simple. Could be a function.
while len(sys.argv) > 1:
    arg = sys.argv.pop(1)
    if arg == '-a':
        optionA = True
    elif arg == '-m':
        optionM = True
    elif arg == '-n':
        optionN = True
    elif arg == '-b':
        optionB = True
    elif arg == '-c':
        try:
            # There are possibility for failure here - no argument, not integer
            optionNumber = int(sys.argv.pop(1))
            if optionNumber < 1:
                raise ValueError
        except:
            usage()
    elif filename is None:
        filename = arg
    else:
        usage()
        
        
# functions
def average(lst):
    if not lst:
        return 0
    return sum(lst) / len(lst)

def median(lst):
    if not lst:
        return 0
    
    lst = sorted(lst)
    n = len(lst)
    mid = n // 2
    
    if n % 2 == 0:
        return (lst[mid - 1] + lst[mid]) / 2
    else:
        return lst[mid]

def obs(lst):
    return len(lst)

def biggest(lst):
    return max(lst)
    
# Working with the options
if filename is None:
    usage("Hey, you need a filename")
else:
    print("Using this file:", filename)
    df = pd.read_csv(filename, sep='\t', header=None)
if optionNumber is not None:
    print("And the number is:", optionNumber)    
    num_list = df[optionNumber].tolist()
else: 
    num_list = df.iloc[:,1:].to_numpy().ravel().tolist()
if optionA:
    print(f"the average number is:\n{average(num_list)}")
if optionM:
    print(f"the median number is:\n{median(num_list)}")    
if optionN: 
    print(f"the number of obeservations is\n{obs(num_list)}")
if optionB:
    print(f"the biggest number is\n{biggest(num_list)}")


