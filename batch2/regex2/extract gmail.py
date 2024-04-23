'''Write a Python function that extracts all email addresses from a
given string using regex and returns them as a list.
'''
import re
string=input("enter a sentence")
output=re.findall('[a-zA-Z0-9]+@[a-zA-Z0-9]+.[a-zA-Z]+',string)#sequence to extract gmail
print(output)