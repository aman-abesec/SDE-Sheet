#======================================================
#      42. Trapping Rain Water
#      https://leetcode.com/problems/trapping-rain-water/
#      https://youtu.be/UZG3-vZlFM4
#=========================================================
class Solution:
    def trap(self, heights: List[int]) -> int:
        l=[0]*len(heights)
        r=[0]*len(heights)
        lm=heights[0]
        rm=heights[len(heights)-1]
        c=0
        for i in range(len(heights)):
            lm=max(lm,heights[i])
            l[i]=lm
        for i in range(len(heights)-1,-1,-1):
            rm=max(rm,heights[i])
            r[i]=rm
        for i in range(len(heights)):
            c+=min(l[i],r[i])-heights[i]
        return c
