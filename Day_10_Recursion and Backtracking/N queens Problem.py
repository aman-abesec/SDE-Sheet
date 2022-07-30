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
