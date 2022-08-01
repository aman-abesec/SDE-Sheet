#=================================================
#        Rod Cutting
#https://practice.geeksforgeeks.org/problems/rod-cutting0840/1
#======================================================

#Method-1(Recursive)
class Solution:
    def solve(self,Larr,Parr,L,N):
        if L==0 or N==0:return 0
        if L>=Larr[N-1]:
            return max(Parr[N-1]+self.solve(Larr,Parr,L-Larr[N-1],N),
            self.solve(Larr,Parr,L,N-1))
        else:
            return self.solve(Larr,Parr,L,N-1)
    def cutRod(self, price, n):
        N=len(price)
        Larr=[i for i in range(1,N+1)]
        return self.solve(Larr,price,n,N)

#Method-2(Memorization)
class Solution:
    def solve(self,Larr,Parr,L,N,dp):
        if L==0 or N==0:return 0
        if dp[N][L]!=-1:return dp[N][L]
        if L>=Larr[N-1]:
            dp[N][L]=max(Parr[N-1]+self.solve(Larr,Parr,L-Larr[N-1],N,dp),
            self.solve(Larr,Parr,L,N-1,dp))
            return dp[N][L]
        else:
            dp[N][L]=self.solve(Larr,Parr,L,N-1,dp)
            return dp[N][L]
    def cutRod(self, price, n):
        N=len(price)
        Larr=[i for i in range(1,N+1)]
        dp=[[-1]*(n+1) for _  in range(N+1)]
        return self.solve(Larr,price,n,N,dp)
