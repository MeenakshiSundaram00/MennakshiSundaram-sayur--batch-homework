lists=[15,4,3,24,44,23,11]
small=lists[0]
for list in lists:
    if(small>list):
        small=list
print(small)