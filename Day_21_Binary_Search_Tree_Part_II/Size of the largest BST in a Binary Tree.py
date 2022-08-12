#=====================================================
#1373. Maximum Size in Binary Tree
#======================================================

import math
class NodeVal:
    def __init__(self,mn,mx,size):
        self.mx=mx
        self.mn=mn
        self.size=size
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        def solve(root):
            if root==None:
                return NodeVal(math.inf,-math.inf,0)
            l=solve(root.left)
            r=solve(root.right)
            if root.val>l.mx and root.val<r.mn:
                return NodeVal(min(root.val,l.mn),max(root.val,r.mx),l.size+r.size+1)
            return NodeVal(-math.inf,math.inf,max(l.size,r.size))
        return solve(root).size
