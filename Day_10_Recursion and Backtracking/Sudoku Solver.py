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




        
