#========================================================
#      72. Edit Distance
#https://practice.geeksforgeeks.org/problems/maximum-sum-increasing-subsequence4749/1
#https://www.geeksforgeeks.org/maximum-sum-increasing-subsequence-dp-14/
#=========================================================


#Method-1
class Solution:
    def solve(self,arr,n,prev):
        if n==0:return 0
        if prev==-1 or arr[n-1]<prev:
            return max(arr[n-1]+self.solve(arr,n-1,arr[n-1]),self.solve(arr,n-1,prev))
        else:
            return self.solve(arr,n-1,prev)
	def maxSumIS(self, Arr, n):
		return self.solve(Arr,n,-1)

#Method-2
dp=[]
class Solution:
    def solve(self,arr,n,prev):
        global dp
        if n==0:return 0
        if dp[n][prev+1]!=-1:return dp[n][prev+1]
        if prev==-1 or arr[n-1]<prev:
            dp[n][prev+1]=max(arr[n-1]+self.solve(arr,n-1,arr[n-1]),self.solve(arr,n-1,prev))
            return dp[n][prev+1]
        else:
            dp[n][prev+1]=self.solve(arr,n-1,prev)
            return dp[n][prev+1]
	def maxSumIS(self, Arr, n):
	    global dp
	    mx=max(Arr)
	    dp=[[-1 for __ in range(mx+2)] for _ in range(n+1)]
		return self.solve(Arr,n,-1)

#Method-3
class Solution:
    def solve(self,arr,n):
        mx=max(arr)
        dp=[[0 for __ in range(mx+3)] for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(-1,mx+2):
                if j==-1 or arr[i-1]<j:
                    dp[i][j+1]=max(arr[i-1]+dp[i-1][arr[i-1]+1],dp[i-1][j+1])
                else:
                    dp[i][j+1]=dp[i-1][j+1]
        # print(dp)
        return dp[n][mx+2]

	def maxSumIS(self, Arr, n):
		return self.solve(Arr,n)

#Method-4
class Solution:
    def solve(self,arr,n):
        sum_array=[i for i in arr]
        for i in range(1,n):
            for j in range(i):
                if arr[i]>arr[j] and sum_array[i]<(sum_array[j]+arr[i]):
                    sum_array[i]=sum_array[j]+arr[i]
        return max(sum_array)


	def maxSumIS(self, Arr, n):
		return self.solve(Arr,n)
5
1 101 2 3 100
3
1 2 3
