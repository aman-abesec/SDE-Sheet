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
