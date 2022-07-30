#========================================================
#      72. Edit Distance
#https://leetcode.com/problems/edit-distance/
#https://www.youtube.com/watch?v=fJaKO8FbDdo&ab_channel=takeUforward
#=========================================================
#Method-1
class Solution:
    def solve(self,s1,s2,n,m):
        global dp
        if m==0 and n!=0:return n
        if n==0 and m!=0:return m
        if n==0 and m==0:return 0
        if dp[n][m]!=-1:return dp[n][m]
        if s1[n-1]==s2[m-1]:
            return self.solve(s1,s2,n-1,m-1)
        else:
            return min(1+self.solve(s1,s2,n-1,m),
                       1+self.solve(s1,s2,n,m-1),
                       1+self.solve(s1,s2,n-1,m-1))
    def minDistance(self, word1: str, word2: str) -> int:
        n=len(word1)
        m=len(word2)
        return self.solve(word1,word2,n,m)

#Method-2
dp=[]
class Solution:
    def solve(self,s1,s2,n,m):
        global dp
        if m==0 and n!=0:return n
        if n==0 and m!=0:return m
        if n==0 and m==0:return 0
        if dp[n][m]!=-1:return dp[n][m]
        if s1[n-1]==s2[m-1]:
            dp[n][m]=self.solve(s1,s2,n-1,m-1)
            return dp[n][m]
        else:
            dp[n][m]=min(1+self.solve(s1,s2,n-1,m),
                       1+self.solve(s1,s2,n,m-1),
                       1+self.solve(s1,s2,n-1,m-1))
            return dp[n][m]
    def minDistance(self, word1: str, word2: str) -> int:
        n=len(word1)
        m=len(word2)
        global dp
        dp=[[-1 for __ in range(m+1)] for _ in range(n+1)]
        return self.solve(word1,word2,n,m)
