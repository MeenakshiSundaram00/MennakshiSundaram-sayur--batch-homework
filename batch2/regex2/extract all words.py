'''Write a Python function that extracts all words (sequences of letters) from a given string using regex and returns them as a list'''
import  re
string=input("enter a string")
output=re.findall('[a-zA-z0-9]+',string)#sequence to extracgt all words
print(output)