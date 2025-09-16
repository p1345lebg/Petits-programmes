running = True
in_game = False

def verify_board_with_direction(board, sign, position, direction : tuple[int,int]):
    x = position[0]+direction[0]
    y = position[1]+direction[1]
    if 0 <= y < 6 or 0 <= x < 7:
        return 0
    if sign == board[y][x]:
        return 1+verify_board_with_direction(board, sign, (x,y), direction)
    return 0
    
def get_board():
    return [[" " for i in range(7)] for i in range(6)] 

def print_board(board):
    for i in board:
        print(i)
    print("   1   2   3   4   5   6   7")
    
board = get_board()
players_signs = ["O", "X"]
current_player = 0 
directions = [
	(1,0),
    (1,1),
    (-1,1),
    (-1,0),
    (-1,-1),
    (1,-1)
]


while running:
    if in_game:
        print_board()
        print(f"player {current_player}")
        ok = False
        y = 5
        while not ok:
            col = (int(input("column : "))-1)%7
            if board[y][col] == " ":
                ok = true
        while board[y-1][col] == " ":
            y-=1
        board[y][col] = players_signs[current_player]
		for d in directions:
            if verify_win:
                truc du winner        
    else:
        print(10*"-")
        input("press enter to retart")
        board = get_board()