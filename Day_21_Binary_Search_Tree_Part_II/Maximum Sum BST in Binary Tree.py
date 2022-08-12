#=====================================================
#1373. Maximum Sum BST in Binary Tree
#https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/
#================================================================

import math
ans=0
class NodeVal:
    def __init__(self,mn,mx,size,ans):
        self.mx=mx
        self.mn=mn
        self.size=size
        self.ans=ans
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        def solve(root):
            if root==None:
                return NodeVal(math.inf,-math.inf,0,0)
            l=solve(root.left)
            r=solve(root.right)
            if root.val>l.mx and root.val<r.mn:
                global ans
                ans=max(ans,l.ans+r.ans+root.val)
                return NodeVal(min(root.val,l.mn),max(root.val,r.mx),l.size+r.size+1,l.ans+r.ans+root.val)
            return NodeVal(-math.inf,math.inf,max(l.size,r.size),l.ans+r.ans)
        # return solve(root).size
        global ans
        ans=0
        solve(root)
        return ans
