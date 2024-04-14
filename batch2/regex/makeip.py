'''3. Same as above, but the input is given without any .
Print all possible ipaddress based on the contraints learnt in problem 1.
eg input - 0000
output 0.0.0.0
input 10026710
output 100.2.67.10
input 100242200
output 100.24.220.0, 100.242.20.0'''
import sys
emp=[]
ans=[]


def check(a,b,c):
    t = int(a)
    i=t
    j = int(b)
    k = int(c)
    if i == 0:
        ans.append(i)
        return 1
    if i*100+j*10+k<255:
        ans.append(i*100+j*10+k)
        return 3
    elif i*100+j*10:
        ans.append(i*10+j)
        return 2
def printer():
    print(*ans,sep=".")

count=0
xin=input("enter a string")
for i in range(len(xin)):
    emp.append(xin[i])
while  len(emp)!=0:
    if count==2:
        if len(emp)==3:
          ans.append(int(emp[0])*10+int(emp[1]))
          ans.append(int(emp[2]))
        if len(emp)==2:
            ans.append(int(emp[0]))
        printer()
        sys.exit(0)
    if len(emp)==2:
      if (emp[0] == "0"):
          ans.append(0)
          ans.append(int(emp[1]))
      else:
          if int(emp[0])*10+int(emp[1])<255:
               ans.append(int(emp[0])*10+int(emp[1]))
          else:
              ans.append(int(emp[0]))
              ans.append(int(emp[1]))
      printer()
      sys.exit(0)
    if len(emp) == 1:
        ans.append(emp[0] )
        printer()
        sys.exit(0)
    value=check(emp[0],emp[1],emp[2])
    if value==3:
        count=count+1
    for j in range(value):
        emp.remove(emp[0])
print(*ans,sep=".")