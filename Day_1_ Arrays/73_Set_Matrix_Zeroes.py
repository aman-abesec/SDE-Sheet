#======================================================
#           73. Set Matrix Zeroes
#  https://leetcode.com/problems/set-matrix-zeroes/
#  https://youtu.be/zgaOU5aInOc
#=========================================================
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r=set()
        c=set()
        rl=len(matrix)
        cl=len(matrix[0])
        for i in range(rl):
            for j in range(cl):
                if matrix[i][j]==0:
                    r.add(i)
                    c.add(j)
        for i in r:
            for j in range(cl):
                matrix[i][j]=0

        for i in c:
            for j in range(rl):
                matrix[j][i]=0

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rl=len(matrix)
        cl=len(matrix[0])
        row=False
        col=False
        for i in range(cl):
            if matrix[0][i]==0:
                row=True

        for i in range(rl):
            if matrix[i][0]==0:
                col=True

        for i in range(1,rl):
            for j in range(1,cl):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    matrix[i][0]=0

        for i in range(1,cl):
            if matrix[0][i]==0:
                for j in range(rl):
                    if matrix[j][i]!=0:
                        matrix[j][i]=0

        for i in range(1,rl):
            if matrix[i][0]==0:
                for j in range(cl):
                    if matrix[i][j]!=0:
                        matrix[i][j]=0
        if row:
            for i in range(cl):
                matrix[0][i]=0
        if col:
            for i in range(rl):
                matrix[i][0]=0
