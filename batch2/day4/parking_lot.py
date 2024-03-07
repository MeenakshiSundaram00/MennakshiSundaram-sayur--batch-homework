import sys
collection=0
def available_free(parking_lot):
    counter=0
    for i in range(len(parking_lot)):
        row=parking_lot[i]
        for j in range(len(row)):
            if(parking_lot[i][j]==0):
               counter=counter+1
    return counter


def assinging_parking_lot(rows,columns):
    parking_lot=[]
    for i in range(rows):
      row=[]
      for j in range(columns):
          row.append(0)
      parking_lot.append(row)
    return parking_lot
def collec():
    return 500
def find_my_vechile(parking_lot,carId):
    for i in range(len(parking_lot)):
        row=parking_lot[i]
        for j in range(len(row)):
           if( parking_lot[i][j]==carId.lower()):
               parking_lot[i][j]=0
               print("your payment included fine has recived")
               print("yor car was dispatched you can recive it in frontyard")
               collection=collec()
               return collection
    print("your vechile is not in the parking lot")
    return

def leaving_parking_lot(carId,row,column,parking_lot,collection):
    if(parking_lot[row][column]==carId.lower()):
        parking_lot[row][column]=0

        print("your payment is recived")
        print("yor car was dispatched you can recive it in frontyard")
        print("thank you for visisting")
        return 100
    yes_or_no=input("do you forgot the any(row and coulmn) parameter (yes/no)")
    if(yes_or_no=="yes"):

        return


def enter_Parking(carId,parking_lot):
    for i in range(len(parking_lot)):
        row=parking_lot[i]
        for j in range(len(row)):
            if parking_lot[i][j]==0:
                parking_lot[i][j]=carId.lower()
                return (str(i)+" "+str(j))
    return "housefull"
rows=int(input("enter no of  rows going to present in the car parking lot"))
column=int(input("enter no of coulmn going to present in the car pparking lot"))
parking_lot=assinging_parking_lot(rows,column)

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
        carNumber=input("enter your carId or car register number of car")
        index=enter_Parking(carNumber,parking_lot)
        indexlist=index.split()
        if('housefull'==indexlist[0]):
            print("parking lot is house full is house full")
        else:
           print("\t\tPARKING LOT")
           print("CARID ",carNumber,sep=":")
           print("Row",indexlist[0],sep=':')
           print("colounm",indexlist[1],sep=":")
           print("don't froget this details")
    elif(option==2):
        carNumber = input("enter your carId or car register number of car")
        rows1=int(input("enter the row  your car placed"))
        if(rows-1<rows1):
            print("invalid input")
            continue

        column1=int(input("enter the column your car placed "))
        if(column-1<column1):
            print("invalid input")
        out=  leaving_parking_lot(carNumber,rows1,column1,parking_lot,collection)
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


        print("allloted lots",(rows*column)-available)
    elif(option==5):
        sys.exit(0)
    else:
        print("invalid input")
