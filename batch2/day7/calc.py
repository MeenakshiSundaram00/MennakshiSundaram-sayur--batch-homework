def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1//num2
list_of_opertor=['+','-','*','/']
list_of_opertor_of_string=[]
string_of_copy=''
string_of_number_and_opertor=input("enter the equation")
for i in range (len( string_of_number_and_opertor)):
    if string_of_number_and_opertor[i] in list_of_opertor:
        list_of_opertor_of_string.append(string_of_number_and_opertor[i])
        string_of_copy=string_of_copy+' '
    else :
        string_of_copy=string_of_copy+string_of_number_and_opertor[i]
int_of_copy_list=string_of_copy.split()
for i in range(len(int_of_copy_list)):
    int_of_copy_list[i]=int(int_of_copy_list[i])

'''if(list_of_opertor_of_string[0]=='*'):
    print(mul(int_of_copy_list[0],int_of_copy_list[1]))
if(list_of_opertor_of_string[0]=='/'):
    print(div(int_of_copy_list[0],int_of_copy_list[1]))
if(list_of_opertor_of_string[0]=='+'):
    print(add(int_of_copy_list[0],int_of_copy_list[1]))
if(list_of_opertor_of_string[0]=='-'):
    print(sub(int_of_copy_list[0],int_of_copy_list[1]))'''
ans=0
#check_condition
while (len(int_of_copy_list)!=1):
    if ("/" in list_of_opertor_of_string):
        index_of_opertor = list_of_opertor_of_string.index('/')
        list_of_opertor_of_string.remove('/')
        ans = div(int_of_copy_list[index_of_opertor], int_of_copy_list[index_of_opertor + 1])
        int_of_copy_list.pop(index_of_opertor + 1)
        int_of_copy_list[index_of_opertor] = ans
        ''' print(int_of_copy_list)
        print(list_of_opertor_of_string)'''
        continue
    elif ("*" in list_of_opertor_of_string):
        index_of_opertor = list_of_opertor_of_string.index('*')
        list_of_opertor_of_string.remove('*')
        ans = mul(int_of_copy_list[index_of_opertor], int_of_copy_list[index_of_opertor + 1])
        int_of_copy_list.pop(index_of_opertor + 1)
        int_of_copy_list[index_of_opertor] = ans
        '''print(int_of_copy_list)
        print(list_of_opertor_of_string)'''
        continue
    elif ("+" in list_of_opertor_of_string):
        index_of_opertor = list_of_opertor_of_string.index('+')
        list_of_opertor_of_string.remove('+')
        ans = add(int_of_copy_list[index_of_opertor], int_of_copy_list[index_of_opertor + 1])
        int_of_copy_list.pop(index_of_opertor + 1)
        int_of_copy_list[index_of_opertor] = ans
        '''print(int_of_copy_list)
        print(list_of_opertor_of_string)'''
        continue
    elif ("-" in list_of_opertor_of_string):
        index_of_opertor = list_of_opertor_of_string.index('-')
        list_of_opertor_of_string.remove('-')
        ans = sub(int_of_copy_list[index_of_opertor], int_of_copy_list[index_of_opertor + 1])
        int_of_copy_list.pop(index_of_opertor + 1)
        int_of_copy_list[index_of_opertor] = ans
        ''' print(int_of_copy_list)
        print(list_of_opertor_of_string)'''
        continue


ans=int_of_copy_list[0]
print("Answer :",ans)

