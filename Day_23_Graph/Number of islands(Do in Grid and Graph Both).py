#=====================================================
#200. Number of Islands
#https://leetcode.com/problems/number-of-islands/
#================================================================

#Using DfS
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(arr,i,j,r,c):
            arr[i][j]="0"
            direction=[[1,0],[0,1],[-1,0],[0,-1]]
            for d in direction:
                m=i+d[0]
                n=j+d[1]
                if m<r and m>=0 and n<c and n>=0 and arr[m][n]=="1":
                    dfs(arr,m,n,r,c)
            
        def solve(grid):
            r=len(grid)
            c=len(grid[0])
            count=0
            for i in range(r):
                for j in range(c):
                    if grid[i][j]=="1":
                        count+=1
                        dfs(grid,i,j,r,c)
            return count
        return solve(grid)
