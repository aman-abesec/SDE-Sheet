#=============================================
#   100. Same Tree
#   https://leetcode.com/problems/same-tree/
#============================================

#T-O(n)
#S-O(n)
class Solution:
    def solve(self,root1,root2):
        if root1==None and root2==None:return True
        if root1==None or root2==None:return False
        if root1.val==root2.val:
            l=self.solve(root1.left,root2.left)
            r=self.solve(root1.right,root2.right)
            if l==True and r==True:return True
            return False
        else:return False
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.solve(p,q)
