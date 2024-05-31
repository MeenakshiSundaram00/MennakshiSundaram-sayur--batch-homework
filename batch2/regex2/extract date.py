'''Write a Python function that extracts all dates (in any format) from a given string using regex and returns them as a list.'''
import re
string=input("enter a senetence")
#output=re.findall('^3[0-1]|2[0-9]|1[0-9]|0[1-9]|[1-9]/1[0-2]|0[1-9]|[0-9]/2[0-9]+$',string)another
output=re.findall('3[0-1]|2[0-9]|1[0-9]|[1-9]/[0-9]/[0-9]',string)
print(output)