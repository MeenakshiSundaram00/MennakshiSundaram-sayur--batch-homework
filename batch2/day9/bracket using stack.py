"""There should be equal open and close paranthesis in input
(A(b)) is correct
())(a) is incorrect
"""
list1=[]
string=input("enter a string")
for i in range(len(string)):
    if(string[i]=="("):
        list1.append("(")
    elif(string[i]==")"):

        try:
           if(list1[-1]=="("):
            list1.pop()
           else:
            list1.append(")")
        except:
            print("invalid")
            exit(0)
if(not list1):
    print("valid")
else :
    print("not valid")