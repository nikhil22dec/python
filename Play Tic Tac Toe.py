#https://www.practicepython.org/exercise/2015/11/26/27-tic-tac-toe-draw.html
def check_winner():
    winner=0
    for j in range(0,3):
        for i in range(1, 3):
            if game[i][j]==game[0][j]:
                  winner=game[0][j]
            else:
                  winner=0
                  break
        if winner > 0:
            print("Winner is: ",winner)
            break
    return winner

game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
count=0
winner=0
while count<9 and winner==0:
    Player1 = input("Player 1, what is your move (in the format row,col)")
    my_list = Player1.split(",")
    x = int(my_list[0])
    y = int(my_list[1])
    if game[x][y] == 0:
        game[x][y] = '1'
    count=count+1
    winner=check_winner()
    if  winner == 0:
        Player2 = input("Player 2, what is your move (in the format row,col)")
        my_list = Player2.split(",")
        x = int(my_list[0])
        y = int(my_list[1])
        if game[x][y] == 0:
            game[x][y] = 2
        count = count + 1
        winner = check_winner()

for i in range(0,3):
    print("\n")
    for j in range(0, 3):
        print(" ",game[i][j]," ",end = '')