import sys
def print_element(list):
    for i in range(25-len(list)):
        print(" ",end='')


def add_menu_item(menu):#function to add item in the menu
     item=input("enter the item")#getting input from user
     item_rate=int(input("enter the item's rate"))#getting rate from user
     menu[item.lower()]=item_rate#addding element to the menu
     yes_or_no=input("do you wanna add again(yes/no)")#asking if the user want to add another element or not
     if("yes"==yes_or_no):#if ->yes call the fuction with passing menu as arugument
         add_menu_item(menu)
     return menu #return menu
def print_menu(menu):#printing the items in the menu
    print(" \t   Menu")
    print("Item\t\t\t\t\tRate")
    for list,listvalue in menu.items():
        print(f"{list}",end='')
        print_element(list)
        print(f"{listvalue}")

def calculate_bill(menu,orderlist):#order the items in the menu

    item=input("enter the item you want")#getting the order from the user`
    if(menu.get(item.lower())==None):#check whether the menu has the item or not
        print("your order not available sir")


    else:#if yes ask for the quantity
        quantity=int(input(f"enter no of {item.upper()} you need "))
        orderlist[item]=quantity#storing the item and quantity as key and value in the dictory
        print("your order has been taken sir")
    yes_or_no = input("do you wanna order any other item (yes/no)")#asking whather the user want to add item or not
    if (yes_or_no == "yes"):#if->yes call the function with updated arugmwnt passing
        calculate_bill(menu,orderlist)
    return orderlist#or returning the orders and quantity

menu={"idly":10,"dosa":20,"poori":15}
order_list={}#decalring the empty dictionary
print("welcome to our Restaurant")
true=1
while true:
    print("------------------------------------------------------------------- ")
    print("1.Add an item to the Menu")
    print("2.print the Menu")
    print("3.Order the product")
    print("End")
    option = int(input("Enter an Option"))#asking inptut from user to current passing
    print("------------------------------------------------------------------- ")
    if(1==option):
        yes_or_no=input("do you wanna add itm to the menu(yes/no)")
        if(yes_or_no=="yes"):
          add_menu_item(menu)
    elif(2==option):
        print_menu(menu)
    elif(3==option):
        total=0
        yes_or_no=input("do you wanna order (yes/no)")
        if(yes_or_no=="yes"):
           order_list= calculate_bill(menu,order_list)
        if (len(order_list) == 0):
            continue
        print("ITEM\t\t\t\t\tQuantity\t\t\t\t\t rate")
        for key,key_value in order_list.items():
            print(f"{key.upper()}")
            print(f"{key.upper()}",end='')
            print_element(key)
            print(      f"{key_value}\t\t\t\t\t\t\t",key_value*(menu.get(key)))
            total+=key_value*(menu.get(key))
        yes_or_no=input("do you have promo code ")
        if ("yes"==yes_or_no):
          promocode=input("enter your code")
          if(promocode=="SAYUR100"):
              print("yoru code is valid")
              print("total including taxes", total +(total *0.03)-(total*0.1))
              continue
          else :
              print("your prmocode is invalid")


        print("total including taxes",total+(total*0.03))
    elif(4==option):
        sys.exit()
    else:
        print("invalid Syntax")

