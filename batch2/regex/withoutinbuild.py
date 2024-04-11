import re
import sys
'''Problem #1
1. Check whether the given string input is a valid ip address.
Find out what are the constraints for an ip address (how many chars, what numbers are allowed, how many '.'
etc)
Write all constraints.
Get an input as string. Return if it is valid or not. 
Use string functions.
'''
ip = []
string = input("enter a ip address")
samp = ""
counter = 0
for i in string:
    if i == ".":
        counter=counter+1
        if int(samp)>255 or int(samp)<0:
            print("invalid")
            sys.exit(0)
        ip.append(int(samp))
        samp = ""
    else:
        samp = samp+i
if counter == 3:
    print("ip address is valid")
else:
    print("ip address is not valid")