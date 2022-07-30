#======================================================
#           75. Sort Colors(Sort an array of 0’s 1’s 2’s)
#  https://leetcode.com/problems/sort-colors/
# https://youtu.be/oaVa-9wmpns
#=========================================================
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        nums.sort()

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        c0=0
        c1=0
        c2=0
        f=0
        for i in nums:
            if i==0: c0+=1
            elif i==1: c1+=1
            else:c2+=1
        while c0>=1:
            nums[f]=0
            f+=1
            c0-=1
        while c1>=1:
            nums[f]=1
            f+=1
            c1-=1
        while c2>=1:
            nums[f]=2
            f+=1
            c2-=1

# # Logic:>
#     if mid==0 swap(beg,mid) and increment both
#     if mid==1 increment mid
#     if mid==2 swap(mid,high) and increment high
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        beg=0
        mid=0
        end=len(nums)-1
        while mid<=end:
            if nums[mid]==0:
                nums[beg],nums[mid]=nums[mid],nums[beg]
                mid+=1
                beg+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[end],nums[mid]=nums[mid],nums[end]
                end-=1
