'''Problem #2
Input is an integer list and another integer k. Output is the k most frequently occuring numbers.
output can be in any order.
eg input = [1,1,1,2,2,3,5,5,5,5], k =2
output [1,5] (top 2 most frequently occuring numbers)
input = [4,5,4,5,4,5,3,3,3,7,8,1,1,1], k = 4
output [4,5,3,1]'''
listofnumbefrs=[]#declaring needed list
copylist=[]
answerlist=[]

def frequencyreader():#count the most repeated numbers and remove it from the list

    counter=0
    num=0
    for i in copylist:
        check=copylist.count(i)

        if check>counter:
            counter=check
            num=i
    answerlist.append(num)
    for i in  range(counter):
        copylist.remove(num)
string=(input("enter element of string"))
listofnumbers=string.split(',')
for i in listofnumbers:
    j=int(i)
    listofnumbefrs.append(j)
key=int(input("enter the no numbers you want to find"))
copylist=listofnumbefrs.copy()
for i in range(key):#loopint according to the key value
    frequencyreader()
print(answerlist)