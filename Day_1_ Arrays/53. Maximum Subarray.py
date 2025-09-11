#======================================================
#           53. Maximum Subarray(Kadane’s Algorithm)
#  https://leetcode.com/problems/maximum-subarray/
#  https://youtu.be/w_KEocd__20
#=========================================================
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx=nums[0]
        mx_now=0
        for i in range(len(nums)):
            mx_now=max(mx_now+nums[i],nums[i])
            if mx_now>=mx:
                mx=mx_now
        return mx

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_n=0
        ans=nums[0]
        for i in nums:
            max_n=max(max_n+i,i)
            ans=max(ans,max_n)
        return ans
