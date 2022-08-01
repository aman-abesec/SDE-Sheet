#=================================================
#        #416. Partition Equal Subset Sum
#https://leetcode.com/problems/partition-equal-subset-sum/
#======================================================
#Method-1(Recursion)
class Solution:
    def solve(self,arr,n,k):
        if k==0:return True
        if n==0 and k!=0:return False
        if arr[n-1]<=k:
            return self.solve(arr,n-1,k-arr[n-1]) or self.solve(arr,n-1,k)
        else:
            return self.solve(arr,n-1,k)
    def canPartition(self, nums: List[int]) -> bool:
        s=sum(nums)
        n=len(nums)
        if s%2!=0:
            return False
        return self.solve(nums,n,(s//2))

#Method-2(Memorization)
dp=[]
class Solution:
    def solve(self,arr,n,k):
        global dp
        if k==0:return True
        if n==0 and k!=0:return False
        if dp[n][k]!=-1:return dp[n][k]
        if arr[n-1]<=k:
            dp[n][k]=self.solve(arr,n-1,k-arr[n-1]) or self.solve(arr,n-1,k)
            return dp[n][k]
        else:
            dp[n][k]=self.solve(arr,n-1,k)
            return dp[n][k]
    def canPartition(self, nums: List[int]) -> bool:
        s=sum(nums)
        n=len(nums)
        if s%2!=0:
            return False
        global dp
        dp=[[-1 for i in range(s//2+1)] for _ in range(n+1)]
        return self.solve(nums,n,(s//2))

#Method-3(Tabulation)
class Solution:
    def solve(self,arr,n,k):
        dp=[[False for i in range(k+1)] for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0]=True
        for i in range(1,n+1):
            for j in range(1,k+1):
                if arr[i-1]<=j:
                    dp[i][j]=dp[i-1][j-arr[i-1]] or dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[n][k]
    def canPartition(self, nums: List[int]) -> bool:
        s=sum(nums)
        n=len(nums)
        if s%2!=0:
            return False
        return self.solve(nums,n,(s//2))
