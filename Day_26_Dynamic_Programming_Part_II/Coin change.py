#=================================================
#        322. Coin Change
#https://leetcode.com/problems/coin-change/
#======================================================

#Best Example to know the use of Memorization and Tabulation
#Method-1(Recursive)
import math
class Solution:
    def solve(self,arr,a,n):
        if a==0:return 0
        if a!=0 and n==0:return math.inf
        if arr[n-1]<=a:
            return min(1+self.solve(arr,a-arr[n-1],n),self.solve(arr,a,n-1))
        else:
            return self.solve(arr,a,n-1)

    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        l=self.solve(coins,amount,n)
        if l==math.inf:
            return -1
        else:
            return l

#Method-2(Memorization)
import math
dp=[]
class Solution:
    def solve(self,arr,a,n):
        global dp
        if a==0:return 0
        if a!=0 and n==0:return math.inf
        if dp[n][a]!=-1:return dp[n][a]
        if arr[n-1]<=a:
            dp[n][a]=min(1+self.solve(arr,a-arr[n-1],n),self.solve(arr,a,n-1))
            return dp[n][a]
        else:
            dp[n][a]=self.solve(arr,a,n-1)
            return dp[n][a]

    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        global dp
        dp=[[-1 for __ in range(amount+1)] for _ in range(n+1)]
        l=self.solve(coins,amount,n)
        if l==math.inf:
            return -1
        else:
            return l

#Method-3(Tabulation)
import math
class Solution:
    def solve(self,arr,a,n):
        dp=[[0 for __ in range(a+1)] for _ in range(n+1)]
        for i in range(1,a+1):
            dp[0][i]=math.inf
        # if a==0:return 0
        # if a!=0 and n==0:return math.inf
        for i in range(1,n+1):
            for j in range(1,a+1):
                if arr[i-1]<=j:
                    dp[i][j]=min(1+dp[i][j-arr[i-1]],dp[i-1][j])
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[n][a]

    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        l=self.solve(coins,amount,n)
        if l==math.inf:
            return -1
        else:
            return l
