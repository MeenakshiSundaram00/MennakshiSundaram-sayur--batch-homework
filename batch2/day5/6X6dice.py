import random
#assign the empty lists for postion and points in global scope
list_places_player1=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
list_places_player2=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
players_point=[0,0]
def place1(player,row,column):#placing in the list
    list_places_player1[row][column]=player
    point_player1(row,column)
def point_player1(row,column,):
    if(list_places_player1[row][column]==list_places_player2[row][column]):
        players_point[0] = players_point[0] + 1
    elif(row==0 and column==0):#checking the postion  [0x0]
        if(bool(list_places_player1[row][column])==bool(list_places_player2[row+1][column])):
            players_point[1]=players_point[1]+1
        elif(bool(list_places_player1[row][column])==bool(list_places_player2[row][column+1])):
            players_point[1] = players_point[1] + 1
    elif (row == 5 and column == 0):#checking the postion [5x0]
            if (bool(list_places_player1[row][column]) == bool(list_places_player2[row-1][column])):
                players_point[1] = players_point[1] + 1
            elif (bool(list_places_player1[row][column]) == bool(list_places_player2[row][column + 1])):
                players_point[1] = players_point[1] + 1
    elif(row==0 and column==5):#checking the postion [0x5]
        if(bool(list_places_player1[row][column])==bool(list_places_player2[row+1][column])):
            players_point[1]=players_point[1]+1
        elif(bool(list_places_player1[row][column])==bool(list_places_player2[row][column-1])):
            players_point[1] = players_point[1] + 1
    elif(row==5 and column==5):#checking the postion [5x5]
        if(bool(list_places_player1[row][column])==bool(list_places_player2[row-1][column])):
            players_point[1]=players_point[1]+1
        elif(bool(list_places_player1[row][column])==bool(list_places_player2[row][column-1])):
            players_point[1] = players_point[1] + 1
    elif(row==5):#checking the postion [5x dont care]
        if (bool(list_places_player1[row][column]) == bool(list_places_player2[row - 1][column])):
            players_point[1] = players_point[1] + 1
        elif (bool(list_places_player1[row][column]) == bool(list_places_player2[row][column - 1])):
            players_point[1] = players_point[1] + 1
        elif(bool(list_places_player1[row][column])==bool(list_places_player2[row][column+1])):
                players_point[1] = players_point[1] + 1
    elif (row == 0):#checking the postion [0x dont care]
        if (bool(list_places_player1[row][column]) == bool(list_places_player2[row +1][column])):
            players_point[1] = players_point[1] + 1
        elif (bool(list_places_player1[row][column]) == bool(list_places_player2[row][column - 1])):
            players_point[1] = players_point[1] + 1
        elif (bool(list_places_player1[row][column]) == bool(list_places_player2[row][column + 1])):
            players_point[1] = players_point[1] + 1
    elif (column == 5):#checking the postion [dont carex 5]
        if (bool(list_places_player1[row][column]) == bool(list_places_player2[row - 1][column])):
            players_point[1] = players_point[1] + 1
        elif (bool(list_places_player1[row][column]) == bool(list_places_player2[row][column - 1])):
            players_point[1] = players_point[1] + 1
        elif (bool(list_places_player1[row][column]) == bool(list_places_player2[row+1][column ])):
            players_point[1] = players_point[1] + 1
    elif (column == 0):#checking the postion [dont carex0]
        if (bool(list_places_player1[row][column]) == bool(list_places_player2[row + 1][column])):
            players_point[1] = players_point[1] + 1
        elif (bool(list_places_player1[row][column]) == bool(list_places_player2[row-1][column ])):
            players_point[1] = players_point[1] + 1
        elif (bool(list_places_player1[row][column]) == bool(list_places_player2[row][column + 1])):
            players_point[1] = players_point[1] + 1
    else:#checking foe the nearby boxes
        if (bool(list_places_player1[row][column]) == bool(list_places_player2[row + 1][column])):
            players_point[1] = players_point[1] + 1
        elif(bool(list_places_player1[row][column]) == bool(list_places_player2[row -1][column])):
            players_point[1] = players_point[1] + 1
        elif(bool(list_places_player1[row][column]) == bool(list_places_player2[row ][column+1])):
            players_point[1] = players_point[1] + 1
        elif(bool(list_places_player1[row][column]) == bool(list_places_player2[row ][column-1])):
            players_point[1] = players_point[1] + 1
'''' doing the above step for player2'''
def place2(player, row, column):
    list_places_player2[row][column] = player
    point_player2(row, column)
def point_player2(row, column, ):
    if (list_places_player2[row][column] == list_places_player1[row][column]):
        players_point[1] = players_point[1] + 1

    elif (row == 0 and column == 0):
        if (bool(list_places_player2[row][column]) == bool(list_places_player2[row + 1][column])):
            players_point[0] = players_point[0] + 1
        elif (bool(list_places_player2[row][column]) == bool(list_places_player1[row][column + 1])):
            players_point[0] = players_point[0] + 1
    elif (row == 5 and column == 0):
        if (bool(list_places_player2[row][column]) == bool(list_places_player1[row - 1][column])):
            players_point[0] = players_point[0] + 1
        elif (bool(list_places_player2[row][column]) == bool(list_places_player1[row][column + 1])):
            players_point[0] = players_point[0] + 1
    elif (row == 0 and column == 5):
        if (bool(list_places_player2[row][column]) == bool(list_places_player1[row + 1][column])):
            players_point[0] = players_point[0] + 1
        elif (bool(list_places_player2[row][column]) == bool(list_places_player1[row][column - 1])):
            players_point[0] = players_point[0] + 1
    elif (row == 5 and column == 5):
        if (bool(list_places_player2[row][column]) == bool(list_places_player1[row - 1][column])):
            players_point[0] = players_point[0] + 1
        elif (bool(list_places_player2[row][column]) == bool(list_places_player1[row][column - 1])):
            players_point[0] = players_point[0] + 1
    elif (row == 5):
        if (bool(list_places_player2[row][column]) == bool(list_places_player1[row - 1][column])):
            players_point[0] = players_point[0] + 1
        elif (bool(list_places_player2[row][column]) == bool(list_places_player1[row][column - 1])):
            players_point[0] = players_point[0] + 1
        elif (bool(list_places_player2[row][column]) == bool(list_places_player1[row][column + 1])):
            players_point[0] = players_point[0] + 1
    elif (row == 0):
        if (bool(list_places_player2[row][column]) == bool(list_places_player1[row + 1][column])):
            players_point[0] = players_point[0] + 1
        elif (bool(list_places_player2[row][column]) == bool(list_places_player1[row][column - 1])):
            players_point[0] = players_point[0] + 1
        elif (bool(list_places_player2[row][column]) == bool(list_places_player1[row][column + 1])):
            players_point[0] = players_point[0] + 1
    elif (column == 5):
        if (bool(list_places_player2[row][column]) == bool(list_places_player1[row - 1][column])):
            players_point[0] = players_point[0] + 1
        elif (bool(list_places_player2[row][column]) == bool(list_places_player1[row][column - 1])):
            players_point[0] = players_point[0] + 1
        elif (bool(list_places_player2[row][column]) == bool(list_places_player1[row+1][column ])):
            players_point[0] = players_point[0] + 1
    elif (column == 0):
        if (bool(list_places_player2[row][column]) == bool(list_places_player1[row + 1][column])):
            players_point[0] = players_point[0] + 1
        elif (bool(list_places_player2[row][column]) == bool(list_places_player1[row-1][column ])):
            players_point[0] = players_point[0] + 1
        elif (bool(list_places_player2[row][column]) == bool(list_places_player1[row][column + 1])):
            players_point[0] = players_point[0] + 1
    else:
        if (bool(list_places_player2[row][column]) == bool(list_places_player1[row + 1][column])):
            players_point[0] = players_point[0] + 1
        elif (bool(list_places_player2[row][column]) == bool(list_places_player1[row - 1][column])):
            players_point[0] = players_point[0] + 1
        elif (bool(list_places_player2[row][column]) == bool(list_places_player1[row ][column+1])):
            players_point[0] = players_point[0] + 1
        elif (bool(list_places_player2[row][column]) == bool(list_places_player1[row][column - 1])):
            players_point[0] = players_point[0] + 1
while(players_point[0]<5 and players_point[1]<5):
    print("player1's turn")
    print("enter any key to to roll the dice")
    key=input()
    row=random.randint(0,5)
    print("rolled value row is",row)
    print("enter any key to to roll the dice again")
    key = input()
    column=random.randint(0,5)
    print("rolled value column is", column)
    place1("a",row,column)

    print("player1's point",players_point[0])
    print("player2's turn")
    print("enter any key to to roll the dice")
    key = input()
    row = random.randint(0, 5)
    print("rolled value row is", row)
    print("enter any key to to roll the dice again")
    key = input()
    column = random.randint(0, 5)
    print("rolled value colum is", column)
    place2("b", row, column)
    print("player2's point", players_point[1])
if(players_point[0]>players_point[1]):
    print("player1 won")
else :
    print("player2 won")