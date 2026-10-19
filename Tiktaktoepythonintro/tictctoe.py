import tkinter as tk
from tkinter import font

"""welcome to TicTacToe game made by Linus"""

#step1 lager tittel til tictactoe displayet og intialiserer bruken av tkinter
class TicTacToeBoard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic-Tac-Toe- Game")
        self._cells = {}
        #step6 these to lines adds a display and grid of cells
        self._create_board_display()
        self._create_board_grid()

#step2 selvekoden som lager display og åpner greien i termialen
    def _create_board_display(self):
        display_frame = tk.Frame(master=self)
        display_frame.pack(fill=tk.X)
        self.display = tk.Label(
            master=display_frame,
            text="Ready?",
            font=font.Font(size=28, weight="bold"),
        )
        self.display.pack()

#step3 this just makes so code is visible and makes a frame to hold the grid with cells in main window
    def _create_board_grid(self):
        grid_frame = tk.Frame(master=self)
        grid_frame.pack()
        #step4 makes the button and row a 9 by 9 aquare to look like a tictactoe board
        for row in range(3):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=75)
            for col in range(3):
                button = tk.Button(
                    master=grid_frame,
                    text="",
                    font=font.Font(size=36, weight="bold"),
                    fg="black",
                    width=3,
                    height=2,
                    highlightbackground="lightblue",
                #step5 makes it possible to clik and use the button class and places the button and fills the grid
                )
                self._cells[button] = (row, col)
                button.grid(
                        row=row,
                        padx=5,
                        pady=5,
                        sticky="nsew"
                    )

if __name__ == "__main__":
    game = TicTacToeBoard()
    game._create_board_display()
    game._create_board_grid()
    game.mainloop()








