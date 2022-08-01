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



        return self.solve(grid,0,0,m,n)

#Method-3(Tabulation)
import math
class Solution:
    def solve(self,mat,m,n):
        #Cornear Case
        if m==1 and n==1:return mat[0][0]
        dp=[[0 for __ in range(m+1)] for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if i==n-1 or j==m-1:dp[n-1][m-1]=mat[n-1][m-1]
                d=mat[i][j]
                if i+1<n:d+=dp[i+1][j]
                else:d+=math.inf-200*100
                l=mat[i][j]
                if j+1<m:l+=dp[i][j+1]
                else:l+=math.inf-200*100
                dp[i][j]=min(d,l)
        return dp[0][0]
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid[0])
        n=len(grid)
        return self.solve(grid,m,n)
