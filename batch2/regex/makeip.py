'''3. Same as above, but the input is given without any .
Print all possible ipaddress based on the contraints learnt in problem 1.
eg input - 0000
output 0.0.0.0
input 10026710
output 100.2.67.10
input 100242200
output 100.24.220.0, 100.242.20.0'''
import sys
import re
list_ip=[]
def valid(ipadd):
    case = re.split(r'\.', ipadd)  # split by dot
    if len(case) == 4:  # check wheather the list contain 4 strings
        for one_value in case:  # loop with all words in the list
            if re.search(r"^(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2}|[0-9][0-9]|[0-9])$", one_value):
                continue  # just continue the loop
            else:  # else end the program eith printing invalid ip
              return
    else:  # else end the program eith printing invalid ip
        return

    print(ipadd)  # if all string pass print valid
def ip_maker(list_ip):
        ip=str(list_ip)#create all possbility of ip
        for first in range(0,len( list_ip)-2):
            for sec in range(first+1,len(list_ip)-1):
                for third in range( sec+1,len(list_ip)):
                     for lst in range(third+1,len(list_ip)):
                       inp=ip[0:sec]+"."+ip[sec:third]+"."+ip[third:lst]+"."+ip[lst:]#slice from first to last and add .

                       valid(inp)
list_ip=(input("enter the string"))
ip_maker(list_ip)
