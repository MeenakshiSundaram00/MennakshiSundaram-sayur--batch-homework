"""Write a Python function that extracts all numbers from a given string using regex and returns them as a list."""
import re
string=input("enter a input")
#output=re.findall('\d+',string)#inbuild special sequence to extract  numbers in finfall
output=re.findall('[0-9]+',string)#  sequence to extract  numbers in finfall
print(output)