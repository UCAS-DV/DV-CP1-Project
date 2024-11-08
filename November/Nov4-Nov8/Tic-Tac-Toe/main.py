import random
import time

board = [
    ['-','-','-'],
    ['-','-','-'],
    ['-','-','-']
]

numbered_board = [
    ['0','1','2'],
    ['3','4','5'],
    ['6','7','8']
]


turn = -1

def render_board(numbered):
    if numbered == False:
        for row in board:
            print(row)
    else:
        for row in numbered_board:
            print(row)

def take_space(space,player):
    if board[space // 3][space - ((space // 3) * 3)] != '-':
        return False
    else:
        board[space // 3][space - ((space // 3) * 3)] = player
        return True

print("-~-~-~-~-~-~-~-~Tic/Tac/Toe-~-~-~-~-~-~-~-~")

while True:

    if turn == -1:
        print('If you ever need to be reminded of the space number. Type "-1" to get the numbered board')
        render_board(True)

        input('If you understand, enter anything. ')
        turn = 0

    if turn % 2 == 0:
        player_move = int(input("What space would you like to take: "))

        if player_move == -1:
            render_board(True)
            continue

        if take_space(player_move,'X') == False:
            print("Oops! Seems like that space is taken! Please try again.")
            continue
        else:
            render_board(False)
            turn += 1
    else:           
        if take_space(random.randint(0,8),'O') == False:
            continue
        else:
            print("CPU making move...")  
            render_board(False)
            turn += 1
            

