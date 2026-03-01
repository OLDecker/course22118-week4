#!/usr/bin/env python3
import sys
import pandas as pd

optionA, optionB, optionNumber, optionF, optionM, optionN, optionT = None, None, None, None, None, None, None
filename = None

# functions
def usage(msg=None):
    # Print a message if there was something specific you want to the user. 
    if msg is not None:
        print(msg, "\n")
    print ("Usage: demooption.py [-a] [-b] [-c <integer>] [-f] [-m] [-n] [-t] <filename>")
    # Exit the program. We can not progress. Makes logic easier elsewhere.
    sys.exit(1)

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

def trimmedmean(lst):
    if not lst:
        return 0
    lst = sorted(lst)
    n = len(lst)
    trim = int(n * 0.05)  # 5%
    trimmed = lst[trim:n - trim]
    if not trimmed:
        return 0
    return sum(trimmed) / len(trimmed)

def frequent(lst):
    if not lst:
        return 0
    counts = {}
    for i in lst:
        counts[i] = counts.get(i, 0) + 1 
    return max(counts, key=counts.get)

# Command line parsing
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
    elif arg == '-t':
        optionT = True
    elif arg == '-f':
        optionF = True
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
if optionT:
    print(f"the trimmed mean is\n{trimmedmean(num_list)}")
if optionF:
    print(f"the most frequent number is:\n{frequent(num_list)}")


