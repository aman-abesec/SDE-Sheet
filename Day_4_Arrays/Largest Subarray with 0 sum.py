#======================================================
#      Largest subarray with 0 sum
#      https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1#
#      https://youtu.be/qgizvmgeyUM
#=========================================================
class Solution:
    def maxLen(self, n, arr):
        sm=0
        mx=0
        hash_map=dict()
        for i in range(n):
            sm+=arr[i]
            if sm==0:
                mx=i+1
            else:
                if sm in hash_map:
                    mx=max(mx,i-hash_map.get(sm))
                else:
                    hash_map[sm]=i
        return mx
