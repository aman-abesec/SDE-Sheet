#======================================================
#      37. Sudoku Solver
#      https://leetcode.com/problems/sudoku-solver/
#=========================================================
class Solution:
    def solveSudoku(self, grid: List[List[str]]) -> None:
        def isValid(r,c,val,grid):
            for i in range(9):
                if grid[r][i]==val:return False
                if grid[i][c]==val:return False
                if grid[3*(r//3)+i//3][3*(c//3)+i%3]==val:return False
            return True

        def solve(grid):
            for i in range(9):
                for j in range(9):
                    if grid[i][j]==".":
                        for k in range(1,10):
                            if isValid(i,j,str(k),grid):
                                grid[i][j]=str(k)
                                if solve(grid)==True:
                                    return True
                                else:
                                    grid[i][j]="."
                        return False
            return True
        solve(grid)


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def is_Valid(row,col,ch):
            for i in range(9):
                if board[row][i] == ch: return False
                if board[i][col] == ch: return False
            rowR,colC= 3*(row//3),3*(col//3)
            for r in range(rowR,rowR+3):
                for c in range(colC,colC+3):
                    if board[r][c] == ch: return False
            return True

        def solve():
            for r in range(9):
                for c in range(9):
                    if board[r][c]=='.':
                        for chrt in map(str, range(1,10)):
                            if is_Valid(r,c,chrt):
                                board[r][c]=chrt
                                if solve(): return True
                                board[r][c]='.'
                        return False
            return True

        solve()



        

