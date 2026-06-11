#=============================================
#   987. Vertical Order Traversal of a Binary Tree
#https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
#https://youtu.be/Et9OCDNvJ78
#============================================

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(
        self, root: Optional[TreeNode]
    ) -> List[List[int]]:
        if root is None:
            return []
        nodes = []
        stack = [(root, 0, 0)]  # node, row, column
        while stack:
            node, row, col = stack.pop()
            nodes.append((col, row, node.val))
            if node.left:
                stack.append((node.left, row + 1, col - 1))
            if node.right:
                stack.append((node.right, row + 1, col + 1))
        nodes.sort()

        result = []
        previous_col = None
        for col, row, value in nodes:
            if col != previous_col:
                result.append([])
                previous_col = col

            result[-1].append(value)

        return result


        
