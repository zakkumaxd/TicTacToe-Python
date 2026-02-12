# STILL THE SAME LOGIC, GUI NOT YET APPLIED
from re import L
import tkinter as tk

root = tk.Tk()
root.title("TicTacToe (W/ GUI)")
root.geometry("400x400")

board =[
    [' ']*3,[' ']*3,[' ']*3,
]
player = 'X'

moves = {
    'a1': (0,0), 'a2': (0,1), 'a3': (0,2),
    'b1': (1,0), 'b2': (1,1), 'b3': (1,2),
    'c1': (2,0), 'c2': (2,1), 'c3': (2,2)
}
  
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

status = tk.Label(root, text=f'Player {player}\'s turn', font=('Arial', 14))
status.pack()

buttons = []
frame = tk.Frame(root)
frame.pack()





def btn_click(row, col):
    global player, reset_btn
    if board[row][col] != ' ':
        return
    
    board[row][col] = player
    buttons[row][col].config(text=player, state='disabled')
    
    if win_check():
        status.config(text=f"Player {player} Wins!")
        disable_all()
        reset_btn = tk.Button(root, text="New Game", font=("Arial", 20), command=reset)
        reset_btn.pack()


    elif draw_check():
        status.config(text='Draw!')
        disable_all()
        reset_btn = tk.Button(root, text="New Game", font=("Arial", 20), command=reset)
        reset_btn.pack()

        
    else: 
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
        status.config(text=f'Player {player}\'s turn')
def click_me():
    btn.pack_forget()
    
def disable_all():
    for row in range(len(board)):
        for col in range(len(board[row])):
            buttons[row][col].config(state='disabled')
            
def reset():
    global board, player
    board =[
    [' ']*3,[' ']*3,[' ']*3,
    ]
    player = 'X'
    status.config(text=f'Player {player}\'s turn')
    for row in range(len(board)):
        for col in range(len(board[row])):
            buttons[row][col].config(text=' ', state='normal')
    reset_btn.destroy()

for row in range(len(board)):
    row_btn = []
    for col in range(len(board[row])):
        btn = tk.Button(frame, text=' ', font=('Arial', 20), width=5, height=2, command=lambda r=row, c=col:btn_click(r, c))
        btn.grid(row=row, column=col, padx=2, pady=2)
        row_btn.append(btn)
    buttons.append(row_btn)
    


root.mainloop()
