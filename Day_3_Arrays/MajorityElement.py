#======================================================
#      169. Majority Element
#   https://leetcode.com/problems/majority-element/
#   https://youtu.be/AoX3BPWNnoE
#=========================================================
#T-O(n)
#S-O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map=dict()
        l=len(nums)
        for i in nums:
            hash_map[i]=hash_map.get(i,0)+1
        for key,val in hash_map.items():
            if val>l//2:
                return key

#S-O(1)
#T-O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count,ele=0,0
        for i in nums:
            if count==0:
                ele=i
            if i==ele: count+=1
            else:count-=1
        return ele
