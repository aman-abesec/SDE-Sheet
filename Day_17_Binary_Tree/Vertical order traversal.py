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
from collections import deque
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:return []
        hash_map={}
        q=deque()
        q.append([root,0,0])
        while q:
            node,data,level=q.popleft()
            if data not in hash_map:
                hash_map[data]={level:[node.val]}
            else:
                if level not in hash_map[data]:
                    hash_map[data][level]=[node.val]
                else:
                    hash_map[data][level]+=[node.val]
            if node.left!=None:q.append([node.left,data-1,level+1])
            if node.right!=None:q.append([node.right,data+1,level+1])
        ans={}
        for i in sorted(hash_map):
            for j in sorted(hash_map[i]):
                if i not in ans:
                    ans[i]=sorted(hash_map[i][j])
                else:
                    ans[i]+=sorted(hash_map[i][j])
        return [ans[i] for i in sorted(ans)]


        
