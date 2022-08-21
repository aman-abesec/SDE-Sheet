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
    
#Using BFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(arr,i,j,r,c,visited):
            visited[i][j]=1
            q=deque()
            q.append([i,j])
            direction=[[1,0],[0,1],[-1,0],[0,-1]]
            while q:
                u=q.popleft()
                arr[u[0]][u[1]]="0"
                for k in direction:
                    m=u[0]+k[0]
                    n=u[1]+k[1]
                    if m<r and m>=0 and n<c and n>=0 and arr[m][n]=="1" and visited[m][n]==0:
                        q.append([m,n])
                        visited[m][n]=1
            
        def solve(grid):
            r=len(grid)
            c=len(grid[0])
            count=0
            visited=[[0 for _ in range(c+1)] for __ in range(r+1)]
            for i in range(r):
                for j in range(c):
                    if grid[i][j]=="1" and visited[i][j]==0:
                        count+=1
                        bfs(grid,i,j,r,c,visited)
            return count
        return solve(grid)
