#===========================================================
#98. Validate Binary Search Tree
#https://leetcode.com/problems/validate-binary-search-tree/
#https://youtu.be/f-sj7I5oXEI
#==============================================================

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def solve(root,mn,mx):
            if root==None:return True
            if root.val>mx or root.val<mn:return False
            return root.val <mx and root.val>mn and solve(root.left,mn,root.val) and solve(root.right,root.val,mx)
        return solve(root,-math.inf,math.inf)
