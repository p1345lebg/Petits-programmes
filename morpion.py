runing = True
in_game = False

def clear_board():
    return [[False for i in range(3)] for i in range(3)]


def verify_win_from(board, x, y):
    if board[x][y] == board[(y+1)%3][x] == board[(y+2)%3][x]:
        return True
    if board[x][y] == board[y][(x+1)%3] == board[y][(x+2)%3]:
        return True
    
    if x == y and board[y][x] == board[(y+1)%3][(x+1)%3] == board[(y+2)%3][(x+2)%3]:
        return True
    if x == 3-y and board[y][x] == board[(y+1)%3][(x+2)%3] == board[(y+2)%3][(x+1)%3]:
        return True
        
def print_board(board)

board = []
current_player = 0

while runing:
    if in_game:
        print("board :")
        for i in board:
            print(i)
        print(f"player {current_player}")
        x = int(input("x : "))%3
        y = int(input("y : "))%3
        board[y][x]
        if verify_win_from(board, x, y):
            print(f"winner is player {current_player}")
        current_player = (current_player+1)%3

    else:
        board = clear_board()
        print("board cleared")
        in_game = True
    