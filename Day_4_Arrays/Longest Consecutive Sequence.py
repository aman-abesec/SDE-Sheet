#======================================================
#      128. Longest Consecutive Sequence
#      https://leetcode.com/problems/longest-consecutive-sequence/
#      https://youtu.be/qgizvmgeyUM
#=========================================================
# T:O(n)+O(n)+O(n)
# S:O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        ans = 0
        for i in seen:
            if i-1 not in seen:
                d,c=i,1
                while d+1 in seen:
                    d+=1
                    c+=1
                ans = max(ans,c)
        return ans
