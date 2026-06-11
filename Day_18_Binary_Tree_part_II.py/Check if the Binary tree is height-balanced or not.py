#=============================================
#   110. Balanced Binary Tree
#   https://leetcode.com/problems/balanced-binary-tree/
#============================================

#T-O(n)
#S-O(n)
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def solve(temp):
            if temp==None:return 0
            l = solve(temp.left)
            r = solve(temp.right)
            if l==-1 or r==-1:return -1
            if abs(l-r)>1:return -1
            return 1+max(l,r)
        return solve(root)!=-1
