#==========================================================
#               152. Maximum Product Subarray
#https://leetcode.com/problems/maximum-product-subarray/
#https://youtu.be/z2oH3sHORS4
#https://www.youtube.com/watch?v=jzQ-f2uU0UU&ab_channel=Pepcoding
#=============================================================

# Method-1
#T-O(2^N)
#S-O(h)
class Solution:
    def solve(self,arr,n,ans):
        if n==0:return ans
        l=self.solve(arr,n-1,ans*arr[n-1])
        r=self.solve(arr,n-1,arr[n-1])
        mx=max(l,r)
        return max(ans,mx)
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        return self.solve(nums,n-1,nums[n-1])

# Method-2
# T-O(n)
# S-O(1)
class Solution:
    def solve(self,arr,n):
        result=arr[0]
        mn,mx=arr[0],arr[0]
        for i in range(1,n):
            if arr[i]<0:
                mn,mx=mx,mn
            mn=min(arr[i],mn*arr[i])
            mx=max(arr[i],mx*arr[i])
            result=max(result,mx)
        return result
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        return self.solve(nums,n)

#Method-3
#T-O(n)
#S-O(1)
import math
class Solution:
    def solve(self,arr,n):
        result=-math.inf
        p=1
        for i in range(n):
            p*=arr[i]
            result=max(result,p)
            if p==0:
                p=1
        p=1
        for i in range(n-1,-1,-1):
            p*=arr[i]
            result=max(result,p)
            if p==0:
                p=1
        return result
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        return self.solve(nums,n)
