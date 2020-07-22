#https://www.practicepython.org/exercise/2015/11/16/26-check-tic-tac-toe.html
game = [[2, 2, 1],
        [1, 2, 2],
        [1, 2, 2]]
winner=0
for j in range(0,3):
    print("____________")
    print("game[ 0 ][",j,"]", game[0][j])
    for i in range(1, 3):
        print("game[",i,"][",j,"]",game[i][j])
        if game[i][j]==game[0][j]:
              winner=game[0][j]
        else:
              winner=0
              break
    if winner > 0:
        print(winner)
        break
