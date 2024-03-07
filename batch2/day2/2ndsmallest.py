lists=[15,2,4,3,24,44,23,11]
small=lists[0]
small2=small
for list in lists:
    if(small>list):
        small2=small
        small=list
    elif(small2 > list and list!=small):
        small2=list
print(small2)