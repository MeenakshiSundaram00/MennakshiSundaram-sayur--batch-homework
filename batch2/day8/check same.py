list_of_cahr=["good","ram","dog","abc","bca","god"]
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

    words=[]
    for i in range(len(sorted(new_list))):
        for j in range(i+1,len(new_list)):
            if new_list[i]==new_list[j]:
                if new_list[j] not in words:
                    words.append(new_list[j])

    #print(repeatd_value)
    return  len(words)




list_of_cahr_with_sam=remove_dupliocate_words()
#print(new_list)
sort()
print(check_used_or_not())