#======================================================
#      Subset Sums
#      https://practice.geeksforgeeks.org/problems/subset-sums2234/1
#      https://youtu.be/rYkfBRtMJr8
#=========================================================
#User function Template for python3
class Solution:
	def subsetSums(self, arr, N):
		result=[]
		def subset(arr,sub=[],i=0,s=0):
		    if i==len(arr):
		        result.append(s)
		        return
		    subset(arr,sub,i+1,s)
		    subset(arr,sub+[arr[i]],i+1,s+arr[i])
		subset(arr)
# 		print(result)
        return result
