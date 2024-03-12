#import datetime
''''Parking garage problem
1.Write a program to calculate the revenue generated in a parking garage in a shopping mall

Parking fee is
If you return within 15 mins, its free
Rs 100 for the first hr
Rs 150 for each hr after that.
Fee is calculated in 30 min increments. (meaning, if you spent 25 mins, you will be charged for 30 mins
If you spend 35 mins, you will be charged for one hr)
Get entry time and exit time from customer as input and display the fee.'''
print("entry in railway time")
entry_time=input("enter entry time in H:M")
exit_time=input("enter exit time in H:M")
entry = (entry_time.split(":"))
exit= (exit_time.split(":"))
entry_min=((int(entry[0])*60)+int(entry[1]))
exit_min=((int(exit[0])*60)+int(exit[1]))
revenue_min=exit_min-entry_min
def calculate_revenue(revenue_time):
    if(revenue_time<15):
        return 0
    if(revenue_time<=60):
        if revenue_time<=30:
            return 50
        else:
            return 100
    revenue_time-=60
    revenue=100+(revenue_time/60)*150
    return revenue
fees=calculate_revenue(revenue_min)
print(f"parking fees  is {fees}")