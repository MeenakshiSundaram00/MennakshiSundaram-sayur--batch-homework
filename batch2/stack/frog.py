"""
This was a question asked for me in a real interview

There are frogs walking in a line represented in the form of a list. The numbers in the list are the size of frogs. A frog(at position i) will eat the previous frog (i-1), if the previous frog is smaller in size. Print the alive frogs in the list

Input : [1,2,5,4,3,2,2]
Output : [5,4,3,2,2]
Explanation : Frog (1) ate Frog(0); Frog(2) ate Frog (1). Rest of the frogs are alive
Input : [4,3,3,2,1]
Output : [4,3,3,2,1]"""
list_of_num=[1,3,1,4,1,2,2,1]
stack=[]


def check(insert):
    if(len(stack)==0):#if the stack doesn't have any element just appending the arugument
            stack.append(insert)
    elif(stack[-1]<insert):#if top  is smaller than the arugment pop top and call function
           stack.pop()
           check(insert)
    else:
            stack.append(insert)



#string = input("enter input as a list")
#list_of_char=string.split()
#for i in list_of_char:
 #   list_of_num.append(int(i))
for i in list_of_num:
    check(i)
print(" ".join(map(str,stack)))

