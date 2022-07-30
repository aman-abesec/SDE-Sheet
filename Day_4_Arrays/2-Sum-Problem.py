#======================================================
#      1. Two Sum
#      https://leetcode.com/problems/two-sum/
#      https://youtu.be/dRUpbt8vHpo
#=========================================================
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(1+i,len(nums)):
                s=nums[i]+nums[j]
                if(s==target):
                    return [i,j]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map=dict()
        for i in range(len(nums)):
            d=target-nums[i]
            if d in hash_map:
                return [i,hash_map[d]]
            else:
                hash_map[nums[i]]=i
