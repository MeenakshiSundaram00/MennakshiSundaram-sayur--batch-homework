#code to remove duplicate words.
str1=input("enter a string")#getting a input from user
list=str1.split()
list2=[]
duplicae_remov_string=[]
for str in list:
    if(str not in list2):# check whether the string prsent in the list already or not
       list2.append(str)#concatenate the char
print(" ".join(list2))