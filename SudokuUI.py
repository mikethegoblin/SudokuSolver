from tkinter import *
from sudoku import Sudoku
from error import UnsolvableSudokuError
import tkinter.messagebox

WIDTH = 500
HEIGHT = 500
MARGIN = 25
SIDE = 50
class SudokuUI():

    def __init__(self, master):
        master.title("Sudoku Solver")
        self.game = [[""] * 9 for i in range(9)]
        self.frame1 = Frame(master, width=500, height=500)
        self.frame1.pack(side=LEFT)
        self.frame2 = Frame(master)
        self.frame2.pack(side=LEFT)
        self.frame3 = Frame(master, width=500, height=500)
        self.frame3.pack(side=LEFT)

        self.row, self.col = -1, -1
        self.__initUI()

    def __initUI(self):

        self.canvas1 = Canvas(self.frame1, width=500, height=500)
        self.canvas1.pack(side=LEFT)

        self.label = Label(self.frame2, text="enter sudoku on the left")
        self.label.pack(side=TOP, fill=BOTH)

        self.solve_button = Button(self.frame2, text="Solve Sudoku", command=self.finish_Sudoku)
        self.solve_button.pack(side=TOP, fill=BOTH)

        self.clear_button = Button(self.frame2, text="Clear Grid", command=self.clear_grid)
        self.clear_button.pack(side=BOTTOM, fill=BOTH)

        self.canvas2 = Canvas(self.frame3, width=500, height=500)
        self.canvas2.pack(side=LEFT)
        self.draw_grid()
        self.draw_puzzle()

        self.canvas1.bind("<Button-1>", self.cell_clicked)
        self.canvas1.bind("<Key>", self.key_pressed)

    def is_empty(self):
        '''determines if self.game is empty'''
        for i in range(9):
            for j in range(9):
                if self.game[i][j] != '':
                    return False
        return True

    def draw_grid(self):
        for i in range(10):
            color = "blue" if i % 3 == 0 else "grey"

            X0 = MARGIN + i * SIDE
            Y0 = MARGIN
            X1 = MARGIN + i * SIDE
            Y1 = HEIGHT - MARGIN
            self.canvas1.create_line(X0, Y0, X1, Y1, fill=color)
            self.canvas2.create_line(X0, Y0, X1, Y1, fill=color)

            X0 = MARGIN
            Y0 = MARGIN + i * SIDE
            X1 = WIDTH - MARGIN
            Y1 = MARGIN + i * SIDE
            self.canvas1.create_line(X0, Y0, X1, Y1, fill=color)
            self.canvas2.create_line(X0, Y0, X1, Y1, fill=color)

    def draw_puzzle(self):
        self.canvas1.delete("numbers")
        for i in range(9):
            for j in range(9):
                answer = self.game[i][j]
                if answer != "":
                    x = MARGIN + j * SIDE + SIDE / 2
                    y = MARGIN + i * SIDE + SIDE / 2
                    self.canvas1.create_text(x, y, text=int(answer), tags="numbers", fill="black")

    def draw_puzzle2(self):
        self.canvas2.delete("numbers")
        for i in range(9):
            for j in range(9):
                answer = self.game[i][j]
                if answer != "":
                    x = MARGIN + j * SIDE + SIDE / 2
                    y = MARGIN + i * SIDE + SIDE / 2
                    self.canvas2.create_text(x, y, text=int(answer), tags="numbers", fill="black")

    def cell_clicked(self, event):
        x, y = event.x, event.y

        if (MARGIN < x < WIDTH - MARGIN and MARGIN < y < HEIGHT - MARGIN):
            self.canvas1.focus_set()

            row, col = int((y - MARGIN) // SIDE), int((x - MARGIN) // SIDE)
            if (row, col) == (self.row, self.col):
                self.row, self.col = -1, -1
            else:
                self.row, self.col = row, col

            self.draw_cursor()
            self.draw_puzzle()

    def draw_cursor(self):
        self.canvas1.delete("cursor")
        if self.row >= 0 and self.col >= 0:
            X0 = MARGIN + self.col * SIDE + 1
            Y0 = MARGIN + self.row * SIDE + 1
            X1 = MARGIN + (self.col + 1) * SIDE - 1
            Y1 = MARGIN + (self.row + 1) * SIDE - 1
            self.canvas1.create_rectangle(X0, Y0, X1, Y1, fill="lawn green", tags="cursor")

    def key_pressed(self, event):
        if self.row >= 0 and self.col >= 0:
            if event.keysym in "123456789":
                self.game[self.row][self.col] = event.keysym
            elif event.keysym == "Up" and self.row > 0:
                self.row -= 1
                self.draw_cursor()
            elif event.keysym == "Left" and self.col > 0:
                self.col -= 1
                self.draw_cursor()
            elif event.keysym == "Right" and self.col < 8:
                self.col += 1
                self.draw_cursor()
            elif event.keysym == "Down" and self.row < 8:
                self.row += 1
                self.draw_cursor()
            elif event.keysym == "BackSpace":
                self.game[self.row][self.col] = ""
        self.draw_puzzle()

    def clear_grid(self):
        self.canvas1.delete("cursor")
        self.canvas1.delete("numbers")
        self.canvas2.delete("numbers")
        self.game = [[""] * 9 for i in range(9)]


    def finish_Sudoku(self):
        sudoku_object = Sudoku(self.game)
        try:
            if sudoku_object.complete_sudoku():
                self.game = sudoku_object.sudoku
                self.draw_puzzle2()
            else:
                raise UnsolvableSudokuError("Empty or invalid Sudoku \nPlease enter a valid Sudoku")
        except UnsolvableSudokuError as error:
            tkinter.messagebox.showinfo("Error", error.message)



if __name__ == "__main__":
    root = Tk()
    x = SudokuUI(root)
    root.mainloop()