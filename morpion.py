runing = True
in_game = False

def clear_board(board):
    board = [[False for i in range(3)] for i in range(3)]


def verify_win_from(board, x, y):
    if board[x][y] == board[(x+1)%3][y] == board[(x+2)%3][y]:
        return True
    if board[x][y] == board[x][(y+1)%3] == board[x][(y+2)%3]:
        return True
    
    if x == y and board[x][y] == board[(x+1)%3][(y+1)%3] == board[(x+2)%3][(y+2)%3]:
        return True
    if x == 3-y and board[x][y] == board[(x+1)%3][(y+2)%3] == board[(x+2)%3][(y+1)%3]:
        return True

board = []
current_player = 0

while runing:
    if in_game:
        for i in board:
            print(i)
        print(f"player {current_player}")
        x = int(input("x : "))%3
        y = int(input("y : "))%3
        if verify_win_from(board, x, y):
            print("winner is player {current_player}")
        current_player = (current_player+1)%3

    else:
        clear_board(board)
        in_game = True
    