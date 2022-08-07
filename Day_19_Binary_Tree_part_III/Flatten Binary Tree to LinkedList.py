#=============================================
#   114. Flatten Binary Tree to Linked List
#   https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
#https://youtu.be/sWf7k1x9XR4
#============================================

prev=None
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def solve(r):
            global prev
            if r==None:return
            solve(r.right)
            solve(r.left)
            r.right=prev
            r.left=None
            prev=r
        global prev
        prev=None
        solve(root)
        return prev
