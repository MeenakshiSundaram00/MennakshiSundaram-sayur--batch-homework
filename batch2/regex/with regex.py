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

ip_address = input("enter a ip address to verify") #get input from user
case = re.split(r'\.', ip_address)#split by dot
if len(case)==4:#check wheather the list contain 4 strings
     for one_value in case:#loop with all words in the list
         if re.search(r"^(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2}|[0-9][0-9]|[0-9])$",one_value):
              continue# just continue the loop
         else:#else end the program eith printing invalid ip
              print("invalid ip addreess")
              sys.exit(0)
else:#else end the program eith printing invalid ip
     print("invalid ip addreess")
     sys.exit(0)
print("valid adress")# if all string pass print valid

