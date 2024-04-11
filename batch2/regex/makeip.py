'''3. Same as above, but the input is given without any .
Print all possible ipaddress based on the contraints learnt in problem 1.
eg input - 0000
output 0.0.0.0
input 10026710
output 100.2.67.10
input 100242200
output 100.24.220.0, 100.242.20.0'''
emp=[]
def check(temp):
    if int(temp)>255 or int(temp) <0:
        return False
    else:
        return True
def number(temp):
    return len(temp)
ip=int(input("enter digits"))
while ip:
    value=check(str(ip%1000).zfill(3))
    if value:
        emp.append(ip%10^(number(str(ip%1000))))
        
    else: