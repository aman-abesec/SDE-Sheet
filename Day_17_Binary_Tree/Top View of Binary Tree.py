#=============================================
#   Top View of Binary Tree
#https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1
#https://youtu.be/Et9OCDNvJ78
#============================================

#T-O(n)
#S-O(n)
from collections import deque
class Solution:
    def topView(self, root):
        hash_map = {}
        que = deque()
        que.append([root,0])
        ans = []
        while que:
            node,index=que.popleft()
            if index not in hash_map:hash_map[index]=node.data
            if node.left:que.append([node.left,index-1])
            if node.right:que.append([node.right,index+1])
        for data in sorted(hash_map):
            ans.append(hash_map[data])
        return ans
