#========================================================
#      300. Longest Increasing Subsequence
#https://leetcode.com/problems/longest-increasing-subsequence/
#Striver Video
#=========================================================
#Method-1(Recursive)
#T-O(2^n)
#S-O(N)
class Solution:
    def solve(self,arr,i,p,n):
        if i==n:return 0
        if p==-1 or arr[p]<arr[i]:
            return max(1+self.solve(arr,i+1,i,n),self.solve(arr,i+1,p,n))
        else:
            return self.solve(arr,i+1,p,n)

    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        return self.solve(nums,0,-1,n)

#Method-2(Memorization)
#T-O(N*N)
#S-O(N)
dpMat=[]
class Solution:
    def solve(self,arr,i,p,n):
        global dpMat
        if i==n:return 0
        if dpMat[i][p+1]!=-1: return dpMat[i][p+1]
        if p==-1 or arr[p]<arr[i]:
            dpMat[i][p+1]=max(1+self.solve(arr,i+1,i,n),self.solve(arr,i+1,p,n))
            return dpMat[i][p+1]
        else:
            dpMat[i][p+1]=self.solve(arr,i+1,p,n)
            return dpMat[i][p+1]

    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        global dpMat
        dpMat=[[-1]*(n+2) for _ in range(n+2)]
        return self.solve(nums,0,-1,n)

#Method-3
#T-O(n^2)
#S-O(n*n)
class Solution:
    def solve(self,arr,n):
        dpMat=[[0]*(n+1) for _ in range(n+1)]
        for k in range(n-1,-1,-1):
            for j in range(k-1,-2,-1):
                if j==-1 or arr[j]<arr[k]:
                    dpMat[k][j+1]= max(1+dpMat[k+1][k+1],dpMat[k+1][j+1])
                else:
                    dpMat[k][j+1]=dpMat[k+1][j+1]
        return dpMat[0][0]

    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        return self.solve(nums,n)

#Method-4
class Solution:
	def lengthOfLIS(self, nums: List[int]) -> int:
		ans = [nums[0]]
		for i in range(1,len(nums)):
			if nums[i] > ans[-1]: ans.append(nums[i])
			else:
				ans[bisect_left(ans,nums[i])]=nums[i]
		return len(ans)

#Method-5
#T-O(n^2)
#S-O(n)
class Solution:
    def solve(self,arr,n):
        dpMat=[1]*(n)
        for i in range(n):
            k=0
            while i>k:
                if arr[i]>arr[k]:
                    dpMat[i]=max(dpMat[i],dpMat[k]+1)
                k+=1
        return max(dpMat)


    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        return self.solve(nums,n)
