#=============================================
#   543. Diameter of Binary Tree
#   https://leetcode.com/problems/diameter-of-binary-tree/
#https://www.youtube.com/watch?v=Rezetez59Nk&ab_channel=takeUforward
#============================================

#T-O(n)
#S-O(height)
import math
mx=-math.inf
class Solution:
    def solve(self,root):
        global mx
        if root==None:return 0
        l=self.solve(root.left)
        r=self.solve(root.right)
        mx=max(mx,l+r)
        return 1+max(l,r)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        global mx
        mx=-math.inf
        self.solve(root)
        return mx
