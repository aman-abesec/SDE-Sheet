#======================================================
#      3. Longest Substring Without Repeating Characters
#      https://leetcode.com/problems/longest-substring-without-repeating-characters/
#      https://youtu.be/qtVh-XEpsJo
#=========================================================
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_start=0
        window_count=0
        hash_map={}
        for window_end in range(len(s)):
            curr_char=s[window_end]
            hash_map[curr_char]=hash_map.get(curr_char,0)+1
            if(len(hash_map)==(window_end-window_start)+1):
                window_count=max(window_count,(window_end-window_start)+1)
            while(len(hash_map)!=(window_end-window_start)+1):
                hash_map[s[window_start]]-=1
                if hash_map[s[window_start]]==0:
                    del hash_map[s[window_start]]
                window_start+=1
        # print(hash_map)
        return window_count
        
