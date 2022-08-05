#=============================================
#   104. Maximum Depth of Binary Tree
#   https://leetcode.com/problems/maximum-depth-of-binary-tree/
#============================================

#We can also used the level order traversal

#T-O(n)
#S-O(h)
class Solution:
    def height(self,root):
        if root==None:return 0
        return 1+max(self.height(root.left),self.height(root.right))
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.height(root)
