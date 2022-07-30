#========================================================
#      Matrix Chain Multiplication
#https://practice.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1
#https://youtu.be/zQrR8t7urEE
#=========================================================

#Method-1
import math
class Solution:
    def solve(self,arr,i,j):
        if i>=j:return 0
        ans=math.inf
        for k in range(i,j):
            temp=self.solve(arr,i,k)+self.solve(arr,k+1,j)+arr[i-1]*arr[k]*arr[j]
            ans=min(ans,temp)
        return ans
    def matrixMultiplication(self, N, arr):
        return self.solve(arr,1,N-1)

#Method-2
import math
dp=[]
class Solution:
    def solve(self,arr,i,j):
        global dp
        if i>=j:return 0
        if dp[i][j]!=-1:return dp[i][j]
        ans=math.inf
        for k in range(i,j):
            temp=self.solve(arr,i,k)+self.solve(arr,k+1,j)+arr[i-1]*arr[k]*arr[j]
            ans=min(ans,temp)
            dp[i][j]=ans
        return ans
    def matrixMultiplication(self, N, arr):
        global dp
        dp=[[-1 for __ in range(101)] for _ in range(101)]
        return self.solve(arr,1,N-1)
