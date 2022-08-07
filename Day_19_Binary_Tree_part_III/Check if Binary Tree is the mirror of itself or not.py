#=============================================
#   Mirror Tree
#  https://practice.geeksforgeeks.org/problems/mirror-tree/1
#============================================

class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self,root):
        def solve(r):
            if r==None:return
            r.left,r.right=r.right,r.left
            solve(r.left)
            solve(r.right)
        solve(root)
        return root
