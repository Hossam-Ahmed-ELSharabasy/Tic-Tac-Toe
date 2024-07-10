import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("لعبة XO - حسام")

        self.player_score = 0
        self.computer_score = 0
        self.board = [""] * 9
        
        self.create_widgets()
        self.reset_board()

    def create_widgets(self):
        self.score_label = tk.Label(self.master, text=f"😊 أنت: {self.player_score} الحاسوب: {self.computer_score} 🤖", font="Arial 15 bold", bg="#cce7e8")
        self.score_label.grid(row=0, column=0, columnspan=3)
        
        self.buttons = []
        for i in range(9):
            button = tk.Button(self.master, text="", font="Arial 20 bold", width=5, height=2, 
                               command=lambda i=i: self.player_move(i), bg="#f7f7f7", activebackground="#e1e1e1")
            button.grid(row=(i//3)+1, column=i%3, padx=5, pady=5)
            self.buttons.append(button)
        
        self.restart_button = tk.Button(self.master, text="إعادة التشغيل 🔄", font="Arial 15 bold", command=self.reset_board, bg="#d4edda", activebackground="#c3e6cb")
        self.restart_button.grid(row=4, column=0, columnspan=3, pady=10)
        
        self.status_label = tk.Label(self.master, text="", font="Arial 15 bold", bg="#cce7e8")
        self.status_label.grid(row=5, column=0, columnspan=3, pady=10)
    
    def reset_board(self):
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="", state=tk.NORMAL, bg="#f7f7f7")
        self.status_label.config(text="")
        
    def player_move(self, index):
        if self.board[index] == "":
            self.board[index] = "X"
            self.buttons[index].config(text="X", state=tk.DISABLED, disabledforeground="#ff5733")
            if self.check_winner("X"):
                self.player_score += 1
                self.update_score()
                self.status_label.config(text="🎉 أنت فزت!")
                self.disable_buttons()
                return
            if "" not in self.board:
                self.status_label.config(text="🤝 تعادل، لا يوجد فائز!")
                return
            self.computer_move()
    
    def computer_move(self):
        available_moves = [i for i, val in enumerate(self.board) if val == ""]
        if available_moves:
            move = random.choice(available_moves)
            self.board[move] = "O"
            self.buttons[move].config(text="O", state=tk.DISABLED, disabledforeground="#007bff")
            if self.check_winner("O"):
                self.computer_score += 1
                self.update_score()
                self.status_label.config(text="الحاسوب فاز! 😞")
                self.disable_buttons()
                return
    
    def check_winner(self, player):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        return any(all(self.board[i] == player for i in cond) for cond in win_conditions)
    
    def update_score(self):
        self.score_label.config(text=f"😊 أنت: {self.player_score} الحاسوب: {self.computer_score} 🤖")
    
    def disable_buttons(self):
        for button in self.buttons:
            button.config(state=tk.DISABLED, bg="#f1f1f1")

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="#cce7e8")
    game = TicTacToe(root)
    root.mainloop()
