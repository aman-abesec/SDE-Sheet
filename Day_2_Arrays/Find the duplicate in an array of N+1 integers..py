#======================================================
#      287. Find the Duplicate Number
#   https://leetcode.com/problems/find-the-duplicate-number/
#   https://youtu.be/32Ll35mhWg0
#=========================================================
#T-O(n)
#S-O(n)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l=set()
        for i in nums:
            if i in l:
                return i
            l.add(i)
#T=O(n)
#S-O(1)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow=nums[0]
        fast=nums[0]
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        fast=nums[0]
        while slow!=fast:
            slow=nums[slow]
            fast=nums[fast]

        return fast
