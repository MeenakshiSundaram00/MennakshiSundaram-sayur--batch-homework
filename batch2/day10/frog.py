string=input()
list_of_char=string.split()
list_of_num=[]
stack=[]
def check(insert):
    try:
        if(stack[-1]<insert):
           stack.pop()
           check(insert)
        else:
            stack.append(insert)

    except:
        stack.append(insert)
for i in list_of_char:
    list_of_num.append(int(i))
for i in list_of_num:
    check(i)
print(" ".join(map(str,(stack))))

