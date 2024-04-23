"""Write a Python function that extracts all URLs from a given string using regex and returns them as a list.
"""
import re
string=input("enter a sentence")
output=re.findall("[a-zA-Z]+//[a-zA-Z.]*[a-zA-Z]+",string)#sequence to extraxt all url
print(output)