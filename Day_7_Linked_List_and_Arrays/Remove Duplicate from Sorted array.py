#======================================================
#      26. Remove Duplicates from Sorted Array
#      https://leetcode.com/problems/remove-duplicates-from-sorted-array/
#      https://youtu.be/Fm_p9lJ4Z_8
#=========================================================
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        prev=nums[0]
        c=0
        for i in range(1,len(nums)):
            if nums[i]!=prev:
                nums[c]=prev
                prev=nums[i]
                c+=1
        nums[c]=nums[i]
        c+=1
        return c
