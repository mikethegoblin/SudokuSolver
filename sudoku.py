
from error import UnsolvableSudokuError
from typing import List


class Sudoku:

    def __init__(self, sudoku: List[List[str]]):
        '''input: a sudoku that needs to be solved
        create 3 dictionaries to record numbers in certain rows, columns, and the 9 3x3 grid(boxes)'''
        self.sudoku = sudoku
        self.columns = {}
        self.rows = {}
        self.boxes = {}
        for x in range(9):
            self.columns[x] = [''] * 9
            self.rows[x] = [''] * 9
            self.boxes[x] = []
        for r in range(len(self.sudoku)):
            for c in range(len(self.sudoku[r])):
                if self.sudoku[r][c] != '':
                    self.rows[r][c] += self.sudoku[r][c]
                    self.columns[c][r] += self.sudoku[r][c]
                    i = self.box_index(r,c)
                    self.boxes[i].append(self.sudoku[r][c])


    # def show_sudoku(self) -> str:
    #     row = 0
    #     ret = ''
    #     for i in range(19):
    #         if i % 2 == 0:
    #             for j in range(9):
    #                 ret += '----'
    #             ret += '\n'
    #         else:
    #             col = 0
    #             for h in range(19):
    #                 if h % 2 == 0:
    #                     ret += '| '
    #                 else:
    #                     ret += self.sudoku[row][col] + ' '
    #                     col += 1
    #             ret += '\n'
    #             row += 1
    #     return ret

    def is_empty(self):
        for i in range(9):
            for j in range(9):
                if self.sudoku[i][j] != "":
                    return False
        return True

    def box_index(self,r,c) -> int:
        if r < 3 and c < 3:
            return 0
        elif r < 3 and 3 <= c < 6:
            return 1
        elif r < 3 and 6 <= c < 9:
            return 2
        elif 3 <= r < 6 and c < 3:
            return 3
        elif 3 <= r < 6 and 3 <= c < 6:
            return 4
        elif 3 <= r < 6 and 6 <= c < 9:
            return 5
        elif 6 <= r < 9 and c < 3:
            return 6
        elif 6 <= r < 9 and 3 <= c < 6:
            return 7
        elif 6 <= r < 9 and 6 <= c < 9:
            return 8
        

    def is_complete(self) -> bool:
        for r in range(len(self.sudoku)):
            for c in range(len(self.sudoku[r])):
                if self.sudoku[r][c] == '':
                    return False
        return True

    def complete_sudoku(self) -> bool:
        '''solve sudoku and return true if given sudoku is solved, false if the sudoku is not solvable'''
        if self.is_empty():
            return False
        elif self.is_complete():
            return True
        else:
            for r in range(len(self.sudoku)):
                for c in range(len(self.sudoku[r])):
                    i = self.box_index(r, c)
                    if self.sudoku[r][c] == '':
                        for x in range(1, 10):
                            num = str(x)
                            if num in self.rows[r] or num in self.columns[c] or num in self.boxes[i]:
                                continue
                            else:
                                self.sudoku[r][c] = num
                                self.rows[r][c] = num
                                self.columns[c][r] = num
                                self.boxes[i].append(num)
                                result = self.complete_sudoku()
                                if result:
                                    return True
                                else:
                                    self.sudoku[r][c] = ''
                                    self.rows[r][c] = ''
                                    self.columns[c][r] = ''
                                    self.boxes[i].remove(num)
                                    continue
                        return False
                            
                

    # def solve_Sudoku(self):
    #     try:
    #         if self.complete_sudoku():
    #             print(self.show_sudoku())
    #         else:
    #             raise UnsolvableSudokuError('this is an unsolvable sudoku!')
    #     except UnsolvableSudokuError as error:
    #         print(error.message)
                    
                            
                    
                    
