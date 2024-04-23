"""Write a Python function that extracts all hashtags
 (words starting with '#') from a given string using regex and returns them as a list."""
import re
string=input("enter a sentence")
output=re.findall('#[A-Za-z0-9]+',string)
print(output)