#=============================================
#   662. Maximum Width of Binary Tree
#https://leetcode.com/problems/maximum-width-of-binary-tree/
#https://youtu.be/ZbybYvcVLks
#============================================

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
import math
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_width = 0
        q=deque()
        q.append([root,0])
        while q:
            l = len(q)
            min_value = math.inf
            max_value = 0
            for _ in range(l):
                data,index=q.popleft()
                min_value = min(min_value,index)
                max_value = max(max_value,index)
                if data.left!=None:q.append([data.left,2*index+1])
                if data.right!=None:q.append([data.right,2*index+2])
            max_width=max(max_width,max_value-min_value+1)
        return max_width 


        
