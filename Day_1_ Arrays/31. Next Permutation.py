#======================================================
#           31. Next Permutation
#  https://leetcode.com/problems/next-permutation/
#  https://youtu.be/LuLCLgMElus Kadane’s Algorithm
#=========================================================
# Steps:>
# 1>find first last index such that a[i]<a[i+1] i.e index2 --1 4 5 3 2
# 2>find index from last such that a[index1]>a[index2]--
# 3>swap index index1 and index2
# 4>reverse all index from index2 to last
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        def reverse(start):
            last=len(nums)-1
            while start<last:
                nums[start],nums[last]=nums[last],nums[start]
                start+=1
                last-=1
        last=len(nums)-2
        while last>=0 and nums[last]>=nums[last+1]:
            last-=1
        if last>=0:
            start=len(nums)-1
            while start>=0 and nums[last]>=nums[start]:
                start-=1
            nums[start],nums[last]=nums[last],nums[start]
        reverse(last+1)
