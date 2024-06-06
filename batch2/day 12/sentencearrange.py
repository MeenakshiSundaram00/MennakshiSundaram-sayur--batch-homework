'''Problem #1
You have list of unique words. you input is a string with no spaces. Return true if the letters in the
input string can be seperated into words that are in the list.
eg list = ["we", "students", "are" ]
input = "wearestudents"
output = true
eg 2 List = ["we", "doctor","and", "nurse", "are"]
input = "wearenurseandoctor"
output = False
input = "wearenurseanddoctor"
output = true'''
import sys

listofstring=[]#declaring the needed list
def counter(string):#count and compare no of character
    val= len(string)
    val2=0
    for i in listofstring:
        for j in i:
            val=val+1
    if val!=val:
        return False
    else:
        return True

def innerelement(stringer,i):#compare thde two string
    if stringer==i:
        return True
    else:
        return False

listforstring=input("list of element")
listofstring=listforstring.split()
string=input("enter the string")
val=counter(string)
if val==False:#if comparison fails fasle will ne print
    print("False")
    sys.exit(0)
for i in range(len(listforstring)):
    for j in listforstring:
        if(innerelement(string[0:len(j)],j)==True):
            string=string[len(j):]
    if not string:
        break
if not string:
    print("true")
else:
    print("false")

