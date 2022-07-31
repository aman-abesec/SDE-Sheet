#=================================================
#        64. Minimum Path Sum
#https://leetcode.com/problems/minimum-path-sum/
#======================================================
#Method-1(Recursive)
import math
class Solution:
    def solve(self,mat,i,j,m,n):
        if i==n-1 and j==m-1:return mat[n-1][m-1]
        if i>=n or m<=j:return math.inf-200*100
        return min(mat[i][j]+self.solve(mat,i+1,j,m,n),mat[i][j]+self.solve(mat,i,j+1,m,n))
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid[0])
        n=len(grid)
        return self.solve(grid,0,0,m,n)

#T-O(n*m)
#S-O(n*m)
#Method-2(Memorization)
dp=[]
import math
class Solution:
    def solve(self,mat,i,j,m,n):
        global dp
        if i==n-1 and j==m-1:return mat[n-1][m-1]
        if i>=n or m<=j:return math.inf-200*100
        if dp[i][j]!=-1:return dp[i][j]
        dp[i][j]=min(mat[i][j]+self.solve(mat,i+1,j,m,n),mat[i][j]+self.solve(mat,i,j+1,m,n))
        return dp[i][j]

    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid[0])
        n=len(grid)
        global dp
        dp=[[-1 for i in range(m+1)] for _ in range(n+1)]
        return self.solve(grid,0,0,m,n)
