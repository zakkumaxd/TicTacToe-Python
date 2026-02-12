import tkinter as tk
import random
import math

root = tk.Tk()
root.title("TicTacToe (W/ GUI)")
root.geometry("400x400")

board = [[' ']*3 for _ in range(3)]
player = 'X'

confetti_particles = []
confetti_active = False

class ConfettiParticle:
    def __init__(self, canvas_width, canvas_height):
        self.x = random.randint(0, canvas_width)
        self.y = random.randint(-canvas_height, 0)
        self.size = random.randint(5, 12)
        self.color = random.choice(['#FF6363', '#6EB5FF', '#63FF95', '#FFE347', '#D67FFF', '#FF954F', '#FF7FDF', '#51FFC3'])
        self.speed = random.randint(3, 8)
        self.swing = random.randint(1, 5)
        self.angle = random.randint(0, 360)
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
    
    def move(self):
        self.y += self.speed
        self.x += math.sin(self.angle) * self.swing
        self.angle += 0.1
        if self.y > self.canvas_height + 20:
            self.y = random.randint(-50, -10)
            self.x = random.randint(0, self.canvas_width)
            self.color = random.choice(['#FF6363', '#6EB5FF', '#63FF95', '#FFE347', '#D67FFF', '#FF954F', '#FF7FDF', '#51FFC3'])

def start_confetti():
    global confetti_active
    confetti_active = True
    confetti_particles.clear()
    for _ in range(50):
        confetti_particles.append(ConfettiParticle(400, 400))
    animate_confetti()

def animate_confetti():
    global confetti_active
    if confetti_active:
        confetti_canvas.delete("confetti")
        for particle in confetti_particles:
            particle.move()
            confetti_canvas.create_oval(
                particle.x, particle.y, 
                particle.x + particle.size, 
                particle.y + particle.size//1.6,
                fill=particle.color, 
                outline="",
                tags="confetti"
            )
        confetti_canvas.tag_raise("confetti")
        confetti_canvas.tag_lower("confetti")
        root.after(50, animate_confetti)

def stop_confetti():
    global confetti_active, confetti_particles
    confetti_active = False
    confetti_particles.clear()
    confetti_canvas.delete("confetti")

def win_check():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return True
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] != ' ':
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

confetti_canvas = tk.Canvas(root, width=400, height=400, highlightthickness=0, bg='white')
confetti_canvas.place(x=0, y=0)

status = tk.Label(root, text=f'Player {player}\'s turn', font=('Arial', 14, 'bold'), bg='white', fg='#000000')
status.pack()

frame = tk.Frame(root, bg='#f5f5fa')
frame.pack(pady=6)

buttons = []

def btn_click(row, col):
    global player
    if board[row][col] != ' ':
        return
    
    board[row][col] = player
    colors = {'X': {'bg': '#1122a8', 'fg': '#000000'}, 'O': {'bg': '#f7ae40', 'fg': '#000000'}}
    buttons[row][col].config(
        text=player, state='disabled',
        bg=colors[player]['bg'], fg='#000000',
        relief='sunken'
    )
    
    if win_check():
        status.config(text=f"Player {player} Wins!", fg='#000000')
        disable_all()
        show_reset_btn()
        start_confetti()
    elif draw_check():
        status.config(text='Draw!', fg='#000000')
        disable_all()
        show_reset_btn()
    else: 
        player = 'O' if player == 'X' else 'X'
        status.config(text=f'Player {player}\'s turn', fg='#000000')

def show_reset_btn():
    global reset_btn
    reset_btn = tk.Button(root, text="New Game", font=("Arial", 20, 'bold'), 
                         bg='white', fg='#000000', relief='ridge', command=reset)
    reset_btn.pack(pady=8)

def disable_all():
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(state='disabled')

def reset():
    global board, player
    board = [[' ']*3 for _ in range(3)]
    player = 'X'
    status.config(text=f'Player {player}\'s turn', fg='#000000')
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text=' ', state='normal', 
                                   bg='#fafbfc', fg='#000000', relief='raised')
    reset_btn.destroy()
    stop_confetti()

for row in range(3):
    row_btn = []
    for col in range(3):
        btn = tk.Button(frame, text=' ', font=('Arial', 20, 'bold'), 
                       width=5, height=2, bg='#fafbfc', fg='#000000', relief='raised',
                       command=lambda r=row, c=col: btn_click(r, c))
        btn.grid(row=row, column=col, padx=4, pady=4)
        row_btn.append(btn)
    buttons.append(row_btn)

confetti_canvas.tag_lower("all")
root.mainloop()
