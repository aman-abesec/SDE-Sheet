#=====================================================
#200. Number of Islands
#https://leetcode.com/problems/number-of-islands/
#================================================================

class Solution:
    def dfs(self,r,c,grid,l,w):
        grid[r][c]="0"
        if c+1<=w and grid[r][c+1]=="1":
            self.dfs(r,c+1,grid,l,w)
        if r+1<=l and grid[r+1][c]=="1":
            self.dfs(r+1,c,grid,l,w)
        if c-1>=0 and grid[r][c-1]=="1":
            self.dfs(r,c-1,grid,l,w)
        if r-1>=0 and grid[r-1][c]=="1":
            self.dfs(r-1,c,grid,l,w)
    def numIslands(self, grid: List[List[str]]) -> int:
        w=len(grid[0])
        l=len(grid)
        ans=0
        for i in range(l):
            for j in range(w):
                if grid[i][j]=="1":
                    ans+=1
                    self.dfs(i,j,grid,l-1,w-1)
        return ans
