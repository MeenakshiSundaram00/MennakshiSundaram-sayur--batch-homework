'''. Check whether the given string input is a valid ip address.
Find out what are the constraints for an ip address (how many chars, what numbers are allowed, how many '.'
etc)
Write all constraints.
Get an input as string. Return if it is valid or not.
Use string functions.

2. Same as above. Use regex.
'''
import re
import sys

string = input("enter a ip address")
x = re.split(r'\.', string)
#print(len(x))
if len(x) != 4:
    print("invalid")
    sys.exit(0)
for i in x:
    if not(i.isnumeric()):
        print("invalid")
        sys.exit(0)
    if int(i) > 255 or int(i) < 0:
        print("invalid")
        sys.exit(0)
print("valid")