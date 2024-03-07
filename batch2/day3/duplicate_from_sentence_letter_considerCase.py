'''Extend the 'remove duplicate' code, to include removing duplicates from words,
 removing duplicates without looking at case'''
def present_or_not(duplicate_string,list):
    for str in list:
        if(duplicate_string in list):
            return False
    return True

sentence=input("enter a sentence ") #getting input from user to remove duplicate from words
list_of_words=sentence.split() #splitting a long string and store it in a list as group of string
without_duplicate=[] #declaring a empty list
for words in list_of_words:#itertaing until it reaches the end of the list
    duplicate_remov_string=''#declaring a mpty string
    for char in words:#iterating until char reaches the end of the string
        if(char.lower() not in duplicate_remov_string.lower()):#check whether the character is already present or not
           duplicate_remov_string += char# if does not prsent add it to the string
    if(present_or_not(duplicate_remov_string,without_duplicate)):
     without_duplicate.append(duplicate_remov_string)# append it to the empty list
#print(*without_duplicate,end='')
print(' '.join(without_duplicate))#printing thr list