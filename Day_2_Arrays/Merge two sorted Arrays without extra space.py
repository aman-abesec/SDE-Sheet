#======================================================
#           88. Merge Sorted Array
#  https://leetcode.com/problems/merge-sorted-array/
#  https://youtu.be/C4oBXLr3zos
#=========================================================

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        ptr1=m-1
        ptr2=n-1
        i=m+n-1
        while ptr2>=0:
            if ptr1>=0 and nums1[ptr1]>nums2[ptr2]:
                nums1[i]=nums1[ptr1]
                ptr1-=1
                i-=1
            else:
                nums1[i]=nums2[ptr2]
                i-=1
                ptr2-=1
