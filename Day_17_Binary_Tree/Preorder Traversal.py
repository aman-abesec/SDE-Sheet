#=============================================
#   144. Binary Tree Preorder Traversal
#https://leetcode.com/problems/binary-tree-preorder-traversal/
#============================================

#Method-1(Recursive)
#T-O(n)
#S-O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        def solve(head):
            if head==None:return
            result.append(head.val)
            solve(head.left)
            solve(head.right)
        solve(root)
        return result

#Method-2(Iterative)
#T-O(n)
#S-O(n)
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        stack=[]
        curr=root
        while curr!=None or stack!=[]:
            while curr!=None:
                stack.append(curr)
                result.append(curr.val)
                curr=curr.left
            curr=stack.pop()
            curr=curr.right
        return result
