#===========================================================
#235. Lowest Common Ancestor of a Binary Search Tree
#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
#==============================================================

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def solve(root,p,q):
            if p==root or q==root:return root
            if root.val>p.val and root.val<q.val or root.val<p.val and root.val>q.val:return root
            if root.val >p.val and root.val>q.val:
                return solve(root.left,p,q)
            else:
                return solve(root.right,p,q)
        return solve(root,p,q)
