#========================================================
#      1143. Longest Common Subsequence
#https://leetcode.com/problems/longest-common-subsequence/
#https://www.youtube.com/watch?v=NPZn9jBrX8U&ab_channel=takeUforward
#=========================================================
#Method-1(Recursive)
#T=O(2^n*2^m)
#T=O(n)
class Solution:
    def solve(self,s1,s2,n,m):
        if m==0 or n==0:return 0
        if s1[n-1]==s2[m-1]:
            return 1+self.solve(s1,s2,n-1,m-1)
        else:
            return max(self.solve(s1,s2,n,m-1),self.solve(s1,s2,n-1,m))

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        return self.solve(text1,text2,n,m)

#Method-2(Memorization)
#T=O(n*m)
#S=O(n*m)
dp=[]
class Solution:
    def solve(self,s1,s2,n,m):
        global dp
        if m==0 or n==0:return 0
        if dp[n][m]!=-1:return dp[n][m]
        if s1[n-1]==s2[m-1]:
            dp[n][m]=1+self.solve(s1,s2,n-1,m-1)
            return dp[n][m]
        else:
            dp[n][m]= max(self.solve(s1,s2,n,m-1),self.solve(s1,s2,n-1,m))
            return dp[n][m]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        global dp
        dp=[[-1]*(m+1) for _ in range(n+1)]
        return self.solve(text1,text2,n,m)

#Method-3(Tabulation)
#T=O(n*m)
#S=O(n*m)
class Solution:
    def solve(self,s1,s2,n,m):
        dp=[[0]*(m+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i][j-1],dp[i-1][j])
        return dp[n][m]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        return self.solve(text1,text2,n,m)
