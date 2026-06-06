#======================================================
#      3. Longest Substring Without Repeating Characters
#      https://leetcode.com/problems/longest-substring-without-repeating-characters/
#      https://youtu.be/qtVh-XEpsJo
#=========================================================
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        start = 0
        ans = 0
        for end in range(len(s)):
            while s[end] in seen:
                seen.remove(s[start])
                start+=1
            seen.add(s[end])
            ans=max(ans,end-start+1)
        return ans
        
