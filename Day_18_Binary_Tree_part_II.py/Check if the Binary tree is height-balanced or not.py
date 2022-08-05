#=============================================
#   110. Balanced Binary Tree
#   https://leetcode.com/problems/balanced-binary-tree/
#============================================

#T-O(n)
#S-O(n)
class Solution:
    def solve(self,root):
        if root==None:return 0
        l=self.solve(root.left)
        r=self.solve(root.right)
        if l==-1 or r==-1:return -1
        if(abs(l-r)>1):return -1
        return 1+max(l,r)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.solve(root)==-1:return False
        return True
