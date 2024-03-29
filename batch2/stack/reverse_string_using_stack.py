"""Reverse a string: Given a string, reverse it using a stack.
Eg : Hello -> olleH"""

string=input("enter a string")
list=[]
for i in string:
    list.append(i)
for i in range(len(list)-1,-1,-1):
    print(list.pop(),end="")