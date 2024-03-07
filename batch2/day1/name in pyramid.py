#name as pyramid
name=input("enter your name:  ")
for i in range(len(name)):
    for j in range(i):
        print(name[j],end='')
    print()