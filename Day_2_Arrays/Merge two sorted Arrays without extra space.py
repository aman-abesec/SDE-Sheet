class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp1 = m-1
        temp2 = n-1
        temp = m + n-1
        while temp2>=0:
            if  temp1>=0 and nums1[temp1]>nums2[temp2]:
                nums1[temp]=nums1[temp1]
                temp1-=1
            else: 
                nums1[temp]=nums2[temp2]
                temp2-=1
            temp-=1