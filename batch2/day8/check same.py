list_of_cahr=["good","ram","dog","abc","bca"]
set_of_char=set()
new_list=[]
list_of_cahr_with_sam=[]

def remove_dupliocate_words():
    for i in list_of_cahr:
        strin=""
        set_of_char=set()
        for x in i:
            set_of_char.add(x)
        for x in set_of_char:
            strin=strin+x
        new_list.append(strin)
    list_of_cahr_with_sam=new_list.copy()

    new_list.clear()
    #print(new_list)
    #print(list_of_cahr_with_sam)
    return list_of_cahr_with_sam

def sort():
    print(list_of_cahr_with_sam)
    for string_ in list_of_cahr_with_sam:
      sort=''.join(sorted(string_))
      new_list.append(sort)
    #print(new_list)

def check_used_or_not():
    #repeatd_value=0

    count = 0
    for i in range(len(new_list)):
        for j in new_list[i + 1:]:

            if new_list[i] == j:
                count += 1
                continue
    return count









    #print(repeatd_value)





list_of_cahr_with_sam=remove_dupliocate_words()
#print(new_list)
sort()
print(check_used_or_not())