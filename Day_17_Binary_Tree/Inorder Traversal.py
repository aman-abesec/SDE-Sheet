#=============================================
#   94. Binary Tree Inorder Traversal
#https://leetcode.com/problems/binary-tree-inorder-traversal/
#============================================

#Method-1(Recursive Soluation)
#T-O(n)
#S-O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        def solve(head):
            if head==None:return
            solve(head.left)
            result.append(head.val)
            solve(head.right)
        solve(root)
        return result

#Method-2(Iterative Soluation)
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        stack=[]
        curr=root
        while curr!=None or stack!=[]:
            while curr!=None:
                stack.append(curr)
                curr=curr.left
            curr=stack.pop()
            result.append(curr.val)
            curr=curr.right
        return result
