board =[
    [' ']*3,[' ']*3,[' ']*3,
]
player = 'X'

moves = {
    'a1': (0,0), 'a2': (0,1), 'a3': (0,2),
    'b1': (1,0), 'b2': (1,1), 'b3': (1,2),
    'c1': (2,0), 'c2': (2,1), 'c3': (2,2)
}

def show_board():
    print('\n  1   2   3')
    print(f"A {board[0][0]} | {board[0][1]} | {board[0][2]}")
    print("  ---------")
    print(f"B {board[1][0]} | {board[1][1]} | {board[1][2]}")
    print("  ---------")
    print(f"C {board[2][0]} | {board[2][1]} | {board[2][2]}\n")

def player_input():
    global player
    while True:
        print()
        move = input("Input position(A1-C3): ").strip().lower()
        if move not in moves:
            print('Invalid position.')
            continue
        row, col  = moves[move]
        if board[row][col] != ' ':
            print("Position taken.")
            continue
        board[row][col] = player

        break
    
def win_check():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return True
        if board[0][i] == board[1][i] == board[2][i] != ' ': # ^ Rows and Cols
            return True
    if board[0][0] == board[1][1] == board[2][2] != ' ': # Diagonal
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ': 
        return True
    return False
    
def draw_check():
    for row in board:
        for col in row:
            if col == ' ':
                return False
    return True

while True:
    show_board()
    player_input()
    
    if win_check():
        print(f"Player {player} Wins!")
        break
        
    if draw_check():
        print("Draw!")
        break
    
    if player == "X":
        player = "O"
    else:
        player = "X"
