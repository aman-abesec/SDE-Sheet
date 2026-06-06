#======================================================
#      18. 4Sum
#      https://leetcode.com/problems/4sum/
#      https://youtu.be/4ggF3tXIAp0
#=========================================================
# T:O(n^3)
# S-O(n)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = set()
        l = len(nums)
        nums.sort()
        for i in range(l):
            for j in range(i+1,l):
                beg = j+1
                end = l-1
                while beg<end:
                    t=nums[i]+nums[j]+nums[beg]+nums[end]
                    if target == t:
                        result.add((nums[i],nums[j],nums[beg],nums[end]))
                        beg+=1
                        end-=1
                    elif target>t:beg+=1
                    else:end-=1
        return list(result)
