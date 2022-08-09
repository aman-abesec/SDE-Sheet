#===========================================================
#700. Search in a Binary Search Tree
#https://leetcode.com/problems/search-in-a-binary-search-tree/
#==============================================================

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def solve(root,val):
            if root==None:return None
            if root.val ==val:return root
            if root.val>val:
                return solve(root.left,val)
            if root.val<val:
                return solve(root.right,val)
        return solve(root,val)
