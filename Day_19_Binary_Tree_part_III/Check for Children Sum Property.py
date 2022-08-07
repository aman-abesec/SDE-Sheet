#=============================================
#   Children Sum Parent
#   https://practice.geeksforgeeks.org/problems/children-sum-parent/1
#============================================

class Solution:
    def isSumProperty(self, root):
        def solve(r):
            if r.left==None and r.right==None:return True
            if r.left==None and r.right!=None:return r.data==r.right.data and solve(r.right)
            if r.left!=None and r.right==None:return r.data==r.left.data and solve(r.left)
            if r.left!=None and r.right!=None:
                return r.data==(r.right.data+r.left.data) and solve(r.right) and solve(r.left)
        if solve(root):return 1
        return 0
