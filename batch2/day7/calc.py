"""Design a calculator with basic operations - add, subtract, multiply and divide.
Get input from user as string and process it.
Start with doing for two numbers and extend multiple number operations if possible. Do not use built in functions like eval."""

def add(num1,num2):#addition of two numbers
    return num1+num2
def sub(num1,num2):#subraction of two numbers
    return num1-num2
def mul(num1,num2):#multiplication of two numbers
    return num1*num2
def div(num1,num2):#divison of two numbers
    return num1//num2
list_of_opertor=['+','-','*','/']#assigning lisgt of variable
list_of_opertor_of_string=[]
string_of_copy=''
string_of_number_and_opertor=input("enter the equation")
for i in range (len( string_of_number_and_opertor)):# seprating operand and opertor
    if string_of_number_and_opertor[i] in list_of_opertor:
        list_of_opertor_of_string.append(string_of_number_and_opertor[i])
        string_of_copy=string_of_copy+' '
    else :
        string_of_copy=string_of_copy+string_of_number_and_opertor[i]
int_of_copy_list=string_of_copy.split()
for i in range(len(int_of_copy_list)):
    int_of_copy_list[i]=int(int_of_copy_list[i])

ans=0
#check_condition
while (len(int_of_copy_list)!=1):#iterating until list of numbers become single element
    if ("/" in list_of_opertor_of_string):#going in the oder of bodmas
        index_of_opertor = list_of_opertor_of_string.index('/')
        list_of_opertor_of_string.remove('/')
        ans = div(int_of_copy_list[index_of_opertor], int_of_copy_list[index_of_opertor + 1])
        int_of_copy_list.pop(index_of_opertor + 1)
        int_of_copy_list[index_of_opertor] = ans
        continue
    elif ("*" in list_of_opertor_of_string):
        index_of_opertor = list_of_opertor_of_string.index('*')
        list_of_opertor_of_string.remove('*')
        ans = mul(int_of_copy_list[index_of_opertor], int_of_copy_list[index_of_opertor + 1])
        int_of_copy_list.pop(index_of_opertor + 1)
        int_of_copy_list[index_of_opertor] = ans
        continue
    elif ("+" in list_of_opertor_of_string):
        index_of_opertor = list_of_opertor_of_string.index('+')
        list_of_opertor_of_string.remove('+')
        ans = add(int_of_copy_list[index_of_opertor], int_of_copy_list[index_of_opertor + 1])
        int_of_copy_list.pop(index_of_opertor + 1)
        int_of_copy_list[index_of_opertor] = ans
        continue
    elif ("-" in list_of_opertor_of_string):
        index_of_opertor = list_of_opertor_of_string.index('-')
        list_of_opertor_of_string.remove('-')
        ans = sub(int_of_copy_list[index_of_opertor], int_of_copy_list[index_of_opertor + 1])
        int_of_copy_list.pop(index_of_opertor + 1)
        int_of_copy_list[index_of_opertor] = ans
        continue
ans=int_of_copy_list[0]
print("Answer :",ans)

