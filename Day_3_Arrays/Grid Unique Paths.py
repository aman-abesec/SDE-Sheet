#======================================================
#      62. Unique Paths
#   https://leetcode.com/problems/unique-paths/
#   https://youtu.be/t_f0nwwdg5o
#=========================================================

# T-O(2^n)
#S-O(2^n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def countpath(row,col):
            if row>=m or col>=n:return 0
            elif row==m-1 and col==n-1:return 1
            else:return (countpath(row+1,col)+countpath(row,col+1))
        return countpath(0,0)

# T-O(m*n)
#S-O(m*n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        v=[[-1]*n for i in range(m)]
        def countpath(row,col):
            if row>=m or col>=n:return 0
            elif row==m-1 and col==n-1:return 1
            else:
                if v[row][col]!=-1:
                    return v[row][col]
                else:
                    v[row][col]=(countpath(row+1,col)+countpath(row,col+1))
                    return v[row][col]
        return countpath(0,0)
#T-O(m-1)
#S-O(1)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        N=n+m-2
        r=m-1
        res1=1
        res2=1
        for i in range(1,r+1):
            res1*=(N-r+i)
            res2*=i
        return res1//res2
