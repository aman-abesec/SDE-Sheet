#=============================================
#   Top View of Binary Tree
#https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1
#https://youtu.be/Et9OCDNvJ78
#============================================

#T-O(n)
#S-O(n)
from collections import deque
class Solution:
    def topView(self,root):
        if root==None:return []
        ans=[]
        hash_map={}
        q=deque()
        q.append([root,0])
        while q:
            node,n=q.popleft()
            if n not in hash_map:
                hash_map[n]=node
            if node.left!=None:q.append([node.left,n-1])
            if node.right!=None:q.append([node.right,n+1])
        for v in sorted(hash_map):
            ans.append(hash_map[v].data)
        return ans
