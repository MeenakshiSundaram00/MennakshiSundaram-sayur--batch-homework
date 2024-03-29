string=input("enter the string")
list=[]
def popper():
    for j in range(len(list) - 1, -1, -1):
        print(list.pop(), end="")

for i in string:
    if(i==" "):
        popper()
        print(" ",end="")
    else:
      list.append(i)
popper()