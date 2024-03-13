'''2.same as parking_gragae1. End the program if 24hrs passes from when the first customer comes in.
Print the total fees collected.'''
import sys
time=[0,0]
parking_lot = []

def time1():
    time[0]=time[0]+6

    if(time[0]==24):
        return False
    return True
def assinging_parking_lot(columns):


    for j in range(columns):
          parking_lot.append(0)

def enter_Parking(carId,parking_lot):
    for i in range(len(parking_lot)):

            if parking_lot[i]==0:
                parking_lot[i]=carId.lower()
                return str(i)
    return "housefull"


def find_my_vechile(parking_lot, carId):
            for i in range(len(parking_lot)):

                if (parking_lot[i] == carId.lower()):
                    parking_lot[i] = 0
                    print("your payment included fine has recived")
                    print("yor car was dispatched you can recive it in frontyard")

                    return 500
            print("your vechile is not in the parking lot")
            return
def leaving_parking_lot(carId,column,parking_lot,collection):
    if(parking_lot[column-1]==carId.lower()):
        parking_lot[column-1]=0

        print("your payment is recived")
        print("yor car was dispatched you can recive it in frontyard")
        print("thank you for visisting")
        return 100
    yes_or_no=input("do you forgot the any(row and coulmn) parameter (yes/no)")
    if(yes_or_no=="yes"):
          find_my_vechile(parking_lot,carId)

column=10
assinging_parking_lot(column)
collection=0
true=True
while(true==True):
    print("\t\t\tMENU")
    print("-------------------------------------")
    print("1.Entering the parking")
    print("2.leaving parking")
    print("3.end session")
    option = int(input("enter your option"))
    print("-------------------------------------")
    if (option == 1):

        carNumber = input("enter your carId or car register number of car")
        index = enter_Parking(carNumber, parking_lot)
        indexlist = index.split()
        if ('housefull' == indexlist[0]):
            print("parking lot is house full is house full")
        else:
            print("\t\tPARKING LOT")
            print("CARID ", carNumber, sep=":")
            # print("Row",indexlist[0],sep=':')
            print("slot", int(indexlist[0]) + 1, sep=":")
            print("don't froget this details")
            true = time1()
    elif (option == 2):

        carNumber = input("enter your carId or car register number of car")
        # rows1=int(input("enter the row  your car placed"))
        # if(rows-1<rows1):
        #   print("invalid input")
        #   continue

        column1 = int(input("enter the slot your car placed "))
        if (column - 1 < column1 - 1):
            print("invalid input")
        out = leaving_parking_lot(carNumber, column1, parking_lot, collection)
        print(out)
        if (out == None):
            out = find_my_vechile(parking_lot, carNumber)
            print(collection)
            if (out == None):
                continue
        collection = collection+out

        true = time1()



    elif (option == 3):
        sys.exit(0)
    else:
        print("invalid input")
print('`````````````````````````````')
print("TODAYS COLLECTION :", collection)
print('`````````````````````````````')

