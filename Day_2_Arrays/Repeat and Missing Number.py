#======================================================
#      268. Missing Number
#   https://leetcode.com/problems/missing-number/
#   https://youtu.be/WnPLSRLSANE
#=========================================================

#T-O(n)
#S-O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xr=0
        for i in range(len(nums)):
            xr^=(nums[i]^(i+1))
        return xr
#T-O(n)
#S-O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sm=0
        for i in range(len(nums)):
            sm-=(nums[i]-(i+1))
        return sm
