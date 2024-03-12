'''3. Same as above, adding more condition.
The parking garage has 10 spaces numbered from 1 to 10.
THere is a car entering or exiting every 10 mins.
When a car enters, you need to tell them which lot is allotted for them.
When the customer comes to pick up the car, get the lot number as input and calculate the fees.

Use arrays if needed.
'''
time=[0,0]
import sys
collection=0
def available_free(parking_lot):
    counter=0
    for i in range(len(parking_lot)):

            if(parking_lot[i]==0):
               counter=counter+1
    return counter


def assinging_parking_lot(columns):
    parking_lot=[]

    for j in range(columns):
          parking_lot.append(0)

    return parking_lot
def collec():
    return 500
def find_my_vechile(parking_lot,carId):
    for i in range(len(parking_lot)):

           if( parking_lot[i]==carId.lower()):
               parking_lot[i]=0
               print("your payment included fine has recived")
               print("yor car was dispatched you can recive it in frontyard")
               collection=collec()
               return collection
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

        return
def time1():
    if(time[1]==60):
        time[1]=0
        time[0]=time+1
    else :
        time[1]=time[1]+10

    if(time[0]==24):
        time[0]=0

    print("time is",time[0],":",time[1])
def enter_Parking(carId,parking_lot):
    for i in range(len(parking_lot)):

            if parking_lot[i]==0:
                parking_lot[i]=carId.lower()
                return str(i)
    return "housefull"
column=10
parking_lot=assinging_parking_lot(column)

while True:
    print("\t\t\tMENU")
    print("-------------------------------------")
    print("1.Entering the parking")
    print("2.leaving parking")
    print("3.getting collection details")
    print("4.current available and filled seats")
    print("5.end session")
    option=int(input("enter your option"))
    print("-------------------------------------")
    if(option==1):
        time1()
        carNumber=input("enter your carId or car register number of car")
        index=enter_Parking(carNumber,parking_lot)
        indexlist=index.split()
        if('housefull'==indexlist[0]):
            print("parking lot is house full is house full")
        else:
           print("\t\tPARKING LOT")
           print("CARID ",carNumber,sep=":")
           #print("Row",indexlist[0],sep=':')
           print("slot",int(indexlist[0])+1,sep=":")
           print("don't froget this details")
    elif(option==2):
        time()
        carNumber = input("enter your carId or car register number of car")
       # rows1=int(input("enter the row  your car placed"))
        #if(rows-1<rows1):
         #   print("invalid input")
         #   continue

        column1=int(input("enter the slot your car placed "))
        if(column-1<column1-1):
            print("invalid input")
        out=  leaving_parking_lot(carNumber,column1,parking_lot,collection)
        print(out)
        if(out==None):
            out=find_my_vechile(parking_lot,carNumber)
            if (out == None):
                continue
        collection=+out
    elif(option==3):
        print('`````````````````````````````')
        print("TODAYS COLLECTION :",collection)
        print('`````````````````````````````')
    elif(option==4):
        available=available_free(parking_lot)
        print("available lots",available)


        print("allloted lots",(column)-available)
    elif(option==5):
        sys.exit(0)
    else:
        print("invalid input")
