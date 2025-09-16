runing = True
in_game = False

def clear_board():
    return [[" " for i in range(3)] for i in range(3)]


def verify_win_from(board, x, y):
    if board[y][x] == board[(y+1)%3][x] == board[(y+2)%3][x]:
        return True
    if board[y][x] == board[y][(x+1)%3] == board[y][(x+2)%3]:
        return True
    
    if x == y and board[y][x] == board[(y+1)%3][(x+1)%3] == board[(y+2)%3][(x+2)%3]:
        return True
    if x == 3-y and board[y][x] == board[(y+1)%3][(x+2)%3] == board[(y+2)%3][(x+1)%3]:
        return True
        
def print_board(board):
    for i in board:
        print(i)

board = []
move_counter = 0
current_player = 0
players_signs = ["O","X"]

while runing:
    if in_game:
        print(10*"-")
        print(f"player {current_player}")
        ok = False
        while not ok:
            x = int(input("x : "))%3
            y = int(input("y : "))%3
            if board[y][x] == " ":
                ok = True
        move_counter += 1
        board[y][x] = players_signs[current_player]
        print_board(board)
        if verify_win_from(board, x, y):
            print(f"winner is player {current_player}")
            in_game = False
        if move_counter >= 9:
            print("tie")
            in_game = False
        current_player = (current_player+1)%2
        

    else:
        input("press any key to restart")
        board = clear_board()
        move_counter = 0
        print("board cleared")
        print_board(board)
        
        in_game = True
    