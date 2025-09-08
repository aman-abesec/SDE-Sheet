#======================================================
#      51. N-Queens
#      https://leetcode.com/problems/n-queens/
#
#=========================================================
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result=[]
        def solve(n,mat,col=[],dig=[],adig=[],i=0):
            if n==i:
                result.append(["".join(_) for _ in mat])
                return
            for j in range(n):
                if j in col or i-j in dig or i+j in adig:
                    continue
                mat[i][j]='Q'
                col.append(j)
                dig.append(i-j)
                adig.append(i+j)
                solve(n,mat,col,dig,adig,i+1)
                mat[i][j]='.'
                col.remove(j)
                dig.remove(i-j)
                adig.remove(i+j)



        mat=[['.']*n for _ in range(n)]
        solve(n,mat)
        return result


#=================
def solveNQueens(n):
    board = [["."] * n for _ in range(n)]
    solutions = []

    def is_safe(row, col):
        # check column
        for r in range(row):
            if board[r][col] == "Q": return False
        # check left diagonal
        r, c = row-1, col-1
        while r >= 0 and c >= 0:
            if board[r][c] == "Q": return False
            r, c = r-1, c-1
        # check right diagonal
        r, c = row-1, col+1
        while r >= 0 and c < n:
            if board[r][c] == "Q": return False
            r, c = r-1, c+1
        return True

    def backtrack(row):
        if row == n:
            solutions.append(["".join(r) for r in board])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row][col] = "Q"
                backtrack(row + 1)
                board[row][col] = "."
    backtrack(0)
    return solutions
