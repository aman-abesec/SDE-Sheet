#=============================================
#   124. Binary Tree Maximum Path Sum
#  https://leetcode.com/problems/binary-tree-maximum-path-sum/
#https://youtu.be/WszrfSwMz58
#============================================

import math
mx=-math.inf
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def solve(r):
            global mx
            if r==None:return 0
            ln=max(0,solve(r.left))
            rn=max(0,solve(r.right))
            mx=max(mx,ln+rn+r.val)
            return r.val+max(ln,rn)
        global mx
        mx=-math.inf
        solve(root)
        return mx
