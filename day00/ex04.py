import sys
import os
import math 

# print(len(sys.argv))        # Total number of arguments

if len(sys.argv) < 3:
    # print(len(sys.argv)) 
    num =  sys.argv[1]
    if num.isdigit() == True:    
        if int(num) % 2 == 0:
            print("is even")
        else :
            print("is odd")
    else:    
        print("AssertionError: argument is not an integer")
else:
    print("AssertionError: more than one argument is provided")