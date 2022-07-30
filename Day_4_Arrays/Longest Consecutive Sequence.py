#======================================================
#      128. Longest Consecutive Sequence
#      https://leetcode.com/problems/longest-consecutive-sequence/
#      https://youtu.be/qgizvmgeyUM
#=========================================================
# T:O(n)+O(n)+O(n)
# S:O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set=set()
        for i in nums:
            hash_set.add(i)
        mx=0
        for j in range(len(nums)):
            if nums[j]-1 not in hash_set:
                curr=nums[j]
                l=1
                while curr+1 in hash_set:
                    curr+=1
                    l+=1
                mx=max(mx,l)
        return mx
