#======================================================
#      18. 4Sum
#      https://leetcode.com/problems/4sum/
#      https://youtu.be/4ggF3tXIAp0
#=========================================================
# T:O(n^3)
# S-O(n)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result=set()
        for i in range(len(nums)):
            if nums[i]>0 and nums[i]>target:
                break
            if(i>0 and nums[i]==nums[i-1]):
                continue
            for j in range(i+1,len(nums)):
                beg=j+1
                end=len(nums)-1
                while beg<end:
                    sm=nums[i]+nums[j]+nums[beg]+nums[end]
                    if sm==target:
                        result.add((nums[i],nums[j],nums[beg],nums[end]))
                        beg+=1
                        end-=1
                    elif sm<target:
                        beg+=1
                    else:
                        end-=1
        return result
