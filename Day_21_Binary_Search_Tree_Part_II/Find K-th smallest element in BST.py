#=====================================================
#230. Kth Smallest Element in a BST
#https://leetcode.com/problems/kth-smallest-element-in-a-bst/
#======================================================

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def solve(root,c,k):
            if root==None:return True
            solv
            e(root.left,c,k)
            c[0]+=1
            if c[0]==k:
                c[1]=root
                return
            solve(root.right,c,k)
        c=[0,None]
        solve(root,c,k)
        return c[1].val
