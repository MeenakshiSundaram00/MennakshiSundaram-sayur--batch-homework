import sys
from datetime import time
from datetime import date
from datetime import datetime

def check_birthday_or_not(current_date,birth_date):

    if(current_date.day==birth_date.day and current_date.month==birth_date.month):
        return True
    return False
def age(current_date,birth_date):
    if(current_date.month>=birth_date.month):
        if(current_date.day>=birth_date.day):
            return current_date.year-birth_date.year
    return current_date.year-birth_date.year-1
def entry_fees(age):
    if(age>=16 and age<=60):
        return 100
    return 50
collc=0
current_date=date.today()
print("\t\t\tWONDERLA TICKET SERVICE")
person=int(input("1.Enter the no of user you need to take ticket"))
for i in range(person):
    print("person",person,"birthday date")
    birth=input("in the format of(dd/mm/yy)")
    birth_date=birth.split("/")
    for i in range(3):
        birth_date[i]=int(birth_date[i])
    if(birth_date[0]>=32 or birth_date[0]<=0 or birth_date[1]>=13 or birth_date[1]<=0 or birth_date[2]>  datetime.now().year):
        print("invalid birthday type")
        sys.exit(0)
    birth_date= date(birth_date[2],birth_date[1],birth_date[0])
    #print(birth_date.year)
    yes_or_no=check_birthday_or_not(current_date,birth_date)
    if(yes_or_no):
        print("its is free for person",i)
        continue
    age_of_user=age(current_date,birth_date)
    collc=collc+entry_fees(age)
if(current_date.weekday()==3 or current_date.weekday()==1):
    collc =collc- (collc*0.2)
    print("after componsation your total bill is",collc)
    sys.exit(0)
print(collc)