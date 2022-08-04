#=============================================
#   145. Binary Tree Postorder Traversal
#https://leetcode.com/problems/binary-tree-postorder-traversal/
#https://youtu.be/k21VKEM8OFY
#============================================

#method-1(Recursive)
#T-O(n)
#S-O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        def solve(head):
            if head==None:return
            solve(head.left)
            solve(head.right)
            result.append(head.val)
        solve(root)
        return  result

#Iterative Using two stck
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        if root==None:return result
        s1=[]
        s2=[]
        s1.append(root)
        while s1!=[]:
            k=s1.pop()
            s2.append(k)
            if k.left!=None:s1.append(k.left)
            if k.right!=None:s1.append(k.right)
        while s2!=[]:
            result.append(s2.pop().val)
        return result
