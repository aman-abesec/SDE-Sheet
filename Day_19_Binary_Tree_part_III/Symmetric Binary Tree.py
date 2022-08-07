#=============================================
#   101. Symmetric Tree
#   https://leetcode.com/problems/symmetric-tree/
#============================================

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def solve(r1,r2):
            if r1==None and r2==None:return True
            if r1==None or r2==None:return False
            if r1.val==r2.val:
                return solve(r1.left,r2.right) and solve(r1.right,r2.left)
            else:
                return False
        return solve(root.left,root.right)
