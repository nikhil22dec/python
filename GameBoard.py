#https://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html
n=int(input('What size game board?'))
for j in range (0,n):
    for i in range (0,n):
        if i<n-1:
            print('|____', end = '')
        else:
            print('|')