#remove duplicat from string
str1=input("enter a string")#getting a input from user
duplicae_remov_string=""
for i in range(len(str1)):
    if(str1[i] not in duplicae_remov_string):# check whether the character prsent in the string already or not
        duplicae_remov_string+=str1[i]#concatenate the char
print(duplicae_remov_string)