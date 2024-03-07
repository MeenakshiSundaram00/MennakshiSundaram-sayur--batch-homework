#3r char have a space
str1=input("enter a string")
for i in range(len(str1)):
    if((i)%2 ==0):#
        print(end=' ')
    print(str1[i],end='')